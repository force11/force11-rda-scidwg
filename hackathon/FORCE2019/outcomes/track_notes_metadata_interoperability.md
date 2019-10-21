**FORCE2019 Research Software Hackathon**

# Metadata interoperability track



## Description

Software Metadata is crucial for many use cases (e.g archive, document, index, share, discover, reuse, reproduce, cite, etc.) but the metadata landscape is vast and many vocabularies and formats exists to capture the metadata.

Metadata interoperability might be the way to harmonize the existing ontologies and facilitate the practice of keeping metadata.

The [CodeMeta](https://codemeta.github.io/) project was established to create a minimal metadata schema for science software and one of its results was CodeMeta crosswalk table which provides a mapping between different software schemas.

One of the The Software Citation Implementation WG task force is the CodeMeta task force. The task force is meeting on the last Wednesday of the month, [last call was on September 25th](https://github.com/force11/force11-sciwg/blob/master/meetings/20190925-codemeta.md).

## Expected (possible) outcomes:

- Review existing CodeMeta tools
- Improve and Hack metadata tools
  - From scratch to codemeta.json
  - Conversion tools between formats
  - BibTeX @software entry and BibLaTeX extension
- Discuss strategy for alignment with schema.org: prepare properties
- Define procedure to include new properties in CodeMeta &amp; CodeMeta sustainability (as part of the Software Citation Implementation WG and its CodeMeta task force)

## Prepared hack and/or documentation:

- Survey of CodeMeta tools:
  - [Working document](https://docs.google.com/spreadsheets/d/1AGdEeYisIMDBtP0B-PT8tY2QpJX6ukMu0E4M_2MgR0k/edit?usp=sharing)
  - [CSV output](CodeMeta_Citation_tools_survey.csv)



## Resources &amp; References:

- [The CodeMeta repository](https://github.com/codemeta/codemeta)
- [List of properties that are not in schema.org](https://codemeta.github.io/terms/#codemeta-terms)
- [Inria&#39;s Bibtex entry proposition](https://gitlab.inria.fr/gt-sw-citation/bibtex-sw-entry)
- [Cite my code chrome extension](https://github.com/citation-file-format/citemycode)

## Attendance (n=10)

| **No** | **Name** | **Affiliation** | **Email** | **discipline(s)** |
| --- | --- | --- | --- | --- |
| 1 | Jen Harrow | ELIXIR-Hub | Jen.harrow@elixir-europe.org |   |
| 2 | Mateusz Kuzak | Netherlands eScience Center | mateusz.kuzak@gmail.com | Life Sciences but no exclusively |
| 3 | Neil Chue Hong | SSI / University of Edinburgh | N.ChueHong@software.ac.uk |   |
| 4 | Martin Fenner | DataCite | mfenner@datacite.org | n/a |
| 5 | Nate Wright | Public Knowledge Project | natew@notthisway.com | n/a |
| 6 | Alisa Surkis | NYU School of Medicine | alisa.surkis@nyulangone.org | biomedical/library |
| 7 | Arfon Smith | STScI/JOSS | arfon.smith@gmail.com | Astronomy &amp; Publishing |
| 8 | Melissa Harrison | eLife | m.harrison@elifesciences.org | Publisher |
| 9 | Chris Chapman | Pentandra | chris@pentandra.com | meta |
| 10 | Valentin Lorentz | Software Heritage | vlorentz@softwareheritage.org | n/a |



## Meeting Notes

- [elife overview](elife_overview.pdf) for intro
- Github repo [codecite form](https://github.com/SoftDev4Research/codecite-form)
- Link to notes from eLife sprint:
  - [Working document online](https://docs.google.com/document/d/1zza21gSszRKE82M__wsKq65R4GKGPvnNrndyYP3jdAk/edit)
  - [Local copy in .docx](elife_sprint.md)
- Key question: does the way we use metadata to support the recognition side if you point to software heritage archive ?
- Metadata needed ?
  - Only needed for citation or also for archiving, versioning,discoverability ?
  - Minimum you need is an identifier DOI?
    - DOI is needed for tracking and citation
  - What do you cite if author hasn&#39;t provided metadata, get from software heritage
- Discussion how deep do you go with citation and how interested are developers in citation ?
  - In general developers would like to be cited for recognition
- Describe a generic workflow for the metadata that is needed
- Is there a tool that checks codemeta.json files to check they have the minimal amount of useful metadata?
- Initial work on a [Chrome bookmarklet](https://github.com/NateWr/citemycode/tree/codemeta_hackathon) to get a bibtex citation for a GitHub repo that includes a codemeta.json file. Further work suggested:
  - Handle missing or malformed data in a codemeta.json file.
  - Use the Github API to get data if no codemeta.json file exists.
  - Support .cff files.
  - Add an \"import to my citation manager\" feature.
  - Support gitlab, software heritage, and other repositories.

### Hack ideas

1. Develop a bookmarklet that generates a citation when you click on it, when on the page of the code repository

    a. Extend existing citemycode bookmarklet to enable it to recognise CodeMeta.json files as well as CFF files
      i. [https://github.com/citation-file-format/citemycode](https://github.com/citation-file-format/citemycode)

    b. Potentially build on [https://citeas.org/](https://citeas.org/) to generate citations based on incomplete information

    c.Hooking into CSL libraries to generate citations in preferred format (Bibtex as base, then others if necessary)
    [ANNOTATION:
    BY &#39;Martin Fenner&#39;
    ON &#39;2019-10-15T10:56:52&#39;
    NOTE: &#39;CSL doesn&#39;t do bibtex.&#39;]

    d. Extend to work on other common public code repositories (GitLab, BitBucket)

    e. Extend to work with [Sofwtare Heritage](https://archive.softwareheritage.org)
    [ANNOTATION:
    BY &#39;Martin Fenner&#39;
    ON &#39;2019-10-15T10:57:47&#39;
    NOTE: &#39;**Is that really needed. If code repositories are updated**.&#39;]
    [ANNOTATION:
    BY &#39;Morane Gruenpeter&#39;
    ON &#39;2019-10-18T10:18:52&#39;
    NOTE: &#39; **If code repository has vanished, I think you want to be able to do so directly from the archived copy.If I understand correctly, this item is about the CiteMyCode bookmarklet**.&#39;]

2. Getting forges (eg. GitHub) to detect files that can be used for citing (eg. codemeta.json or a .cff), and highlight them (like GitHub does when there is a CODE\_OF\_CONDUCT.md)


3. Create a GitHub action to have something which will get triggered on a release / PR? This would go to write a codemeta.json file as a PR which could be reviewed for missing / incorrect metadata

  a. Tool that automatically tests generates codemeta files and files a PR which uses information from GitHub to produce as good a codemeta file as possible for the repo.
  [ANNOTATION:
  BY &#39;Arfon Smith&#39;
  ON &#39;2019-10-15T15:22:20&#39;
  NOTE: &#39;**Code here**: https://github.com/arfon/zenodo-actions&#39;]

  b. Potential to have the action added per organisation, so that people in the organisation are reminded to do this when they create new software

4. Create a tool that checks codemeta.json files to see if it contains the minimal sensible metadata?

5. Create a tool that generates codemeta.json files from CRAN metadata

6. Create a tool that harvests metadata from CFF or codemeta.json (or other LD representation) and generates a nice-looking web page of the information for humans and machines (HTML+RDFa).

7. Create a tool that harvests metadata from a NPM library in GitHub, referenced in JOSS and generate a codemeta.json file

  a. [https://joss.theoj.org/papers/10.21105/joss.01520](https://joss.theoj.org/papers/10.21105/joss.01520)

  b. [https://joss.theoj.org/papers/10.21105/joss.01179](https://joss.theoj.org/papers/10.21105/joss.01179)

  c. [https://joss.theoj.org/papers/10.21105/joss.00698](https://joss.theoj.org/papers/10.21105/joss.00698)
[ANNOTATION:
BY &#39;Arfon Smith&#39;
ON &#39;2019-10-15T12:41:57&#39;
NOTE: &#39;This has a package.json and codemeta.json file&#39;]


Note: Software Heritage has a Python tool to convert from NPM&#39;s package.json to codemeta.json. It should be installable with:

`
sudo pip3 install swh.indexer
`

then run:

`swh indexer mapping translate npm path/to/package.json`

code is available [here](https://forge.softwareheritage.org/source/swh-indexer/browse/master/swh/indexer/metadata_dictionary/npm.py). Ask Valentin for more info.

8. Create a tool that harvests metadata from a Ruby library/project and generate a codemeta.json file.

9. Create a tool that harvests metadata from a project&#39;s web page having pre-existing semantic markup (e.g schema.org and doap) and transforms it into the shape of a codemeta.json file.
  1. [https://pentandra.com/colophon/](https://pentandra.com/colophon/)

### Test repositories

- Generate list of repos which already have codemeta.json files (about 750 on GitHub)
- Perfect use case (already has a good codemeta.json file)
- Decent use case (would be easier to generate a good codemeta.json file)
- Difficult use case (would be hard to generate a good codemeta.json file):
  - [https://github.com/enzo-project/enzo-dev](https://github.com/enzo-project/enzo-dev)
- List of projects with a codemeta.json at root: [https://forge.softwareheritage.org/P549](https://forge.softwareheritage.org/P549)
- [https://github.com/search?q=filename%3Acodemeta.json&amp;type=Code](https://github.com/search?q=filename%3Acodemeta.json&amp;type=Code)
  - Repositories with CodeMeta files which work with CiteMyCode bookmarklet:
    - [https://github.com/ropensci/codemetar](https://github.com/ropensci/codemetar)
  - Repositories with CodeMeta files which don&#39;t work with CiteMyCode:
    - [https://github.com/SimonGreenhill/phylogemetric](https://github.com/SimonGreenhill/phylogemetric)


Creating the mapping between languages, package managers metadata and codemeta metadata (census of most popular metadata files in Software Heritage in 2017: [https://forge.softwareheritage.org/P332](https://forge.softwareheritage.org/P332) ):


### Add vocabularies into the CodeMeta Crosswalk table
Valentin:

scala (too hard, executable that returns metadata)

clojure (PR with crosswalk )

haskell (PR with crosswalk)

Mateusz:

R package (needs conversions, could use existing ropensci/codemetar)

julia (PR with the crosswalk)

PR to the crosswalk table #219-#222: see [https://github.com/codemeta/codemeta/pull/219](https://github.com/codemeta/codemeta/pull/219)

#### Procedure of adding a vocabulary
- check if there is the crosswalk in codemeta
  - if there is one, check if the field types are the same or do they require conversion,
  - if there is no, create one, make a PR to codemeta, find out about conversions
- implement conversion script

### Mandatory fields (decreasing order of importance)l:

1. Structured Author names
2. Title
3. One of:
  - PID (pointing to a specific version),
  - non-PID url,
  - url (in that order)
4. Year
5. Publisher

| **generic** | **.cff** | **datacite** | **.zenodo.json** | **JATS** |
| --- | --- | --- | --- | --- |
| Citation type |   | \<ResourceTyperesourceTypeGeneral=\"Software\"\> |   | \<ref\>\<element-citation publication-type=\"software\"\> |
| Author wrapper |   | \<contributors\>  |   | \<person-group> |
| Author name wrapper |   | \<contributor\> |   | \<name\> |
| Author(s) name as string  | authors:- family-names: Druskat    given-names: Stephan | \<contributorName\> | creators |  \<string-name\>
 |
| Author name, structured |   | \<givenName\>
\<familyName\> |   | \<surname\>\<given-names\> |
| Publication Year | date-released | \<publicationYear\> | created | \<year\> |
| Title wrapper |   | \<titles\> |   |   |
| Title | title | \<title\>  | title | \<data-title\>But subject to change only other current option is \<article-title\> |
| Version No | version | \<version\> | version | \<version\> With optional @attribute value, eg: \<version designator=\"XXX\"\> |
| Publisher (host)\* | - | \<publisher\> | - | \<publisher-name\>Could also add  \<publisher-loc\>Or use \<source\> instead to indicate repo |
| PID URL |   | Identifier |   |   |
| DOI | doi | \<identifier identifierType=\"DOI\"\> | doi | \<pub-id pub-id-type=\"doi\"\> |
| URL (non-PID) |   |   |   | Eg: \<ext-link ext-link-type=\"uri\" xlink:href=\"https://www.globalphasing.com/buster/\"\>https://www.globalphasing.com/buster/\</ext-link\>;  |

\*(host/repo/institution)
