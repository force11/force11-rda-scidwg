################
# Preamble

# For querying the API (need to install python3-requests on your system first)
import requests

# For loading the dataset
import os
import gzip
import json

# Python utility libraries for handling lists
import itertools
import collections

# Imports the "pprint" function, which pretty-prints large objects
from pprint import pprint


def print_box(text):
    border = '+-' + '-'*len(text) + '-+'
    print()
    print(border)
    print('| ' + text + ' |')
    print(border)
    print()


#################
# Getting the dataset
#
# First, we need to download the data from DataCite's API. This will take some time.
# We will also save it locally so we don't need to re-download it next time.

print_box('Getting the dataset')

DATASET_LOCATION = './data/datacite_software.json.gz'

if os.path.isfile(DATASET_LOCATION):
    # We already have a cached copy of the datacite on the filesystem,
    # let's use it
    with gzip.open(DATASET_LOCATION, 'rt') as fd:
        data = json.load(fd)
else:
    # We don't already have a cached copy of the dataset, let's download
    # it from DataCite
    
    # Initial URL; it will get all objects on datasite whose type is "Software"
    url = 'https://api.datacite.org/dois?query=types.resourceTypeGeneral:Software&page[size]=1000&page[cursor]=1'

    # We'll put all the results in this list
    data = []

    while True:
        # Send the request
        headers = {'accept': 'application/vnd.api+json'}
        print('Downloading {}'.format(url))
        response = requests.get(url, headers=headers)

        # Parse results and add them to the set
        j = response.json()
        data.extend(j['data'])

        # Finished?
        if 'next' not in j['links'] or url == j['links']['next']:
            break

        # Continue with next URL
        url = j['links']['next']
    print('Finished downloading dataset.')

    # Write the dataset to the filesystem so we can re-use it later
    with gzip.open(DATASET_LOCATION, 'wt') as fd:
        json.dump(data, fd)
        
all_dois = {x['id'] for x in data}


print('Number of objects in dataset: {}'.format(len(data)))

print('First object in the dataset:')
pprint(data[0])


############
# Relationship between software and versions
#
# DataCite considers "software" both the software itself and each of its versions/release. Fortunately, there are references between the two.

print_box('Relationship between software and versions')


# We can get the set of all DOIs that are target of an "IsVersionOf":
target_of_IsVersionOf = set()
for obj in data:
    if obj['attributes']['relatedIdentifiers']:
        for relation in obj['attributes']['relatedIdentifiers']:
            if relation['relationType'] == 'IsVersionOf':
                target_of_IsVersionOf.add(relation['relatedIdentifier'])


# Count them:
print('Targets of IsVersionOf:', len(target_of_IsVersionOf))

# We can also get the set of all DOIs which have an "HasVersion" relationship:
has_version = set()
for obj in data:
    if obj['attributes']['relatedIdentifiers']:
        if any(relation['relationType'] == 'HasVersion' for relation in obj['attributes']['relatedIdentifiers']):
            has_version.add(obj['id']) 

# There are slightly less:
print('Objects with HasVersion:', len(has_version))

# There is one in the first set that is not in the second one (because its version is not publicly available):
print('Objects with HasVersion but not target of IsVersionOf:', has_version - target_of_IsVersionOf)

# There are 175 the other way around:
missing = target_of_IsVersionOf - has_version
print('Number of targets of IsVersionOf that do not have a HasVersion:', len(missing))

print()

# For some of them, it's because they use an "HasPart" property instead of "HasVersion":
print('Some of them use HasPart instead of HasVersion:')
pprint([x['attributes']['relatedIdentifiers'] for x in data if x['id'] in missing])

# The other ones are missing from the dataset, because they are
# not software (eg. regular dataset).
# They are referenced because some of their versions is
# (probably erroneously) marked as a software

print()

# Let's pick one and analyze it:
example_missing_doi = list(missing - all_dois)[0]
print('Let\'s pick an example missing DOI:', example_missing_doi)

# Here are its relationships:
example_missing = requests.get('https://api.datacite.org/dois/' + example_missing_doi).json()['data']
print('Relations of this object:')
pprint(example_missing['attributes']['relatedIdentifiers'])

# Let's fetch its relationships' type:
print('Its related objects\' type:')
for relation in example_missing['attributes']['relatedIdentifiers']:
    if relation['relatedIdentifierType'] == 'DOI':
        obj = requests.get('https://api.datacite.org/dois/' + relation['relatedIdentifier']).json()['data']
        print(obj['attributes']['types']['resourceTypeGeneral'])


###########
# Analyzing DOI sources

print_box('Analyzing DOI sources')

print('Sources of DOIs:')
pprint(collections.Counter(obj['relationships']['client']['data']['id'] for obj in data))


##########
# Analyzing titles

print_box('Analyzing titles')

list_of_titles = [obj['attributes']['titles'][0]['title'] for obj in data]
print('Number of titles:', len(list_of_titles))  # Same number as the dataset size

# Number of unique titles:
print('Number of unique titles:', len(set(list_of_titles)))

print()

# Most "popular" titles:
counter = collections.Counter(list_of_titles)
print('Most common titles:')
pprint(counter.most_common(10))


#########
## Project uniqueness
#
# As we saw, multiple "software" objects are different version of the same software, and the software itself.
# There is also the possibility of having multiple objects corresponding to the same software.
# It is not easy to find those, but we can do a coarse approximation by deduplicating by project name
# on the most popular software sources.

print_box('Project uniqueness')

# Fetch all URL relations
urls = []
for obj in data:
    if obj['attributes']['relatedIdentifiers']:
        for rel in obj['attributes']['relatedIdentifiers']:
            if rel['relatedIdentifierType'] == 'URL':
                urls.append(rel['relatedIdentifier']) 

print('Number of URLs: {}'.format(len(urls)))
print('Number of unique URLs: {}'.format(len(set(urls))))

print()

# Most popular domains:
counter = collections.Counter(url.split('/')[2] for url in urls if '/' in url)
print('Most common domains:')
pprint(counter.most_common(10))

print()

unique_github_urls = set(url for url in urls if url.startswith('https://github.com/'))
unique_zenodo_urls = set(url for url in urls if url.startswith('https://zenodo.org/'))
print('Unique URLs on Github: {}'.format(len(unique_github_urls)))
print('Unique URLs on Zenodo: {}'.format(len(unique_zenodo_urls)))

# Unique projects on GitHub (we transform
# "https://github.com/Organization/Project/blahblah" into
# ("Organization", "Project"):
unique_github_projects = set(tuple(url.split('/')[3:5]) for url in unique_github_urls)
# Unique projects on GitHub (we transform
# "https://zenodo.org/communities/project/blahblah" into
# "project":
unique_zenodo_projects = set(url.split('/')[4] for url in unique_zenodo_urls)
print('Unique projects on Github: {}'.format(len(unique_github_projects)))
print('Unique projects on Zenodo: {}'.format(len(unique_zenodo_projects)))

# Note that 22811+277 approximately matches the ~23k software "non-version" we found earlier
