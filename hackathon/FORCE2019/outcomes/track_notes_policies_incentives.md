**FORCE2019 Research Software Hackathon**

# Policies and incentives track



## Description:

Making software a first class citizen is only possible if the stakeholders involved create a nurturing habitat for software. There are policy makers that already took action recognizing software as a research output that needs to be evaluated and promoted.

We want to survey the practices already established and see if these practices have improved the software quality or even the overall research quality. This survey could benefit the stakeholders in the academic community and help with recommendations regarding software policies.

Also, international initiatives have engaged in open research (the FAIR principles for example) which have influenced policies and incentives regarding research data and research software.

We can also look at software citation standards as an incentive to receive credit and to promote software as a research output.

## Expected outcomes:

- Survey of practices in institutions, evaluation committees, national research bodies, learned societies, publishers
- Discuss barriers and possible solutions to incentivize software citation

**Resources &amp; References:**

| **Title** | **Description** | **Institution**** /organisation **|** Link **|** Year** |
| --- | --- | --- | --- | --- |
| ACM badges | The ACM badges are an Incentive for quality research artifact, with the following options: functional, reusable, available, results replicated, results reproduced. | ACM | [https://www.acm.org/publications/policies/artifact-review-badging](https://www.acm.org/publications/policies/artifact-review-badging) | 2018 |
| Attributing and Referencing (Research) Software: Best Practices and Outlook from Inria  | This article describes practices at the Inria french national institution.three key recommendations. (1) propose a richer taxonomy for software contributions with a qualitative scale. (2) It is essential to put the human at the heart of the evaluation. (3) Distinguish citation from reference. | Inria | [https://hal.inria.fr/hal-02135891](https://hal.inria.fr/hal-02135891) | 2019 |
| Policy Statement on Software | AAS Journals have adopted a policy that reflects the importance of software to the astronomical community |   | [https://journals.aas.org/policy-statement-on-software/](https://journals.aas.org/policy-statement-on-software/) |   |
| Force11- Software Citation Implementation, Guidance for Authors | Guidance for Authors  | Force11 | [https://doi.org/10.5281/zenodo.3479198](https://doi.org/10.5281/zenodo.3479198)   | 2019 |



## Participants (n=4)

| **No** | **Name** | **Affiliation** | **Email** | **discipline(s)** |
| --- | --- | --- | --- | --- |
| 1 | Dario Taraborelli | Chan Zuckerberg Initiative | dario@chanzuckerberg.com | Open science, open citations, scientific open source |
| 2 | Emmy Tsang | eLife | e.tsang@elifesciences.org | Publishing, open-source for open science, life sciences |
| 3 | Shelley Stall | AGU | sstal@agu.org | Publishing, Society - Culture Change Needed for Digital |
| 4 | Michelle Phillips | ICE Publishing | Michelle.phillips@icepublishing.com | Publishing, policy |

## Summary:

- The group discussion shifted from the original goal of [surveying existing practices and policies](https://github.com/force11/force11-rda-scidwg/blob/master/hackathon/FORCE2019/outcomes/software_best_practices_crosswalk.csv) (which was completed by the other track) to a review of pain points and &quot;known unknowns&quot; in software archiving practices.
- We discussed, in particular, the burden that software archiving / citation policies may put on researchers and authors, given the variety of available policies and the lack of usable tools for making these workflows accessible to the least computationally skilled researchers.
- One key question we discussed was the appropriate place for incentivizing software archiving/citation practices: should this happen at the code repository level? Or during the submission process for a manuscript or a journal? The answer to that question—which, arguably, some additional user research can shed light on—will inform the right priorities in terms of tooling and user interfaces.
- In particular, knowing that the vast majority of research code lives on GitHub [citation needed], we suggested that creating a shortlist of high-priority features that would reduce usability barriers or increase the adoption of these practices among researchers would be a desirable next step.

## Meeting Notes:

- Credit for research engineers, what&#39;s the state of evaluation practices in different countries?
- Big initiative by major publishers to commit to shared best practices, but there is still a significant gap in compliance with schemas to support data and software citation.
  - Enabling FAIR Data Project - Requiring data and software citation in publication within the Earth, space, and environmental sciences.
    - [Commitment Statement](https://copdess.org/enabling-fair-data-project/commitment-statement-in-the-earth-space-and-environmental-sciences/)
    - [Author Guidelines for Data](https://copdess.org/enabling-fair-data-project/author-guidelines/)
- Researchers/authors are at loss about how to comply with new policies/best practices. Even the very basic understanding of what a repository is, or why software needs metadata, seems to be lacking, and this creates a major burden among authors to comply with recommendations.
- Repository Finder [https://repositoryfinder.datacite.org](https://repositoryfinder.datacite.org) helps you identify possible hosters for code by domain

#### What needs to be captured:

- Version that was used in the paper
- Repository (where the code/software is living) - current version
- USAGE of the software - a counter? Akin to datacount
  - \# forking
  - \# downloads
  - \# citation
  - Provenance
  - Social media?

#### Stakeholders and incentives

- Researchers: checklist – something easy to use and adopt
  - If funding bodies and publishers make this mandatory, then people will want guidelines on how to satistfy funders/publishers&#39; requirements
- Publishers
- Funding bodies
- Institutions
- National research bodies

#### Potential problems/exclusions to policies:

- Some researchers (e.g. in climate science) may not want to be associated with certain pieces of research or software/code - can we address this fear?

### Research software developers/engineers

What they don&#39;t currently think about, but are important:

- Metadata/Vocabulary for describing software – to facilitate reuse and discovery
  - Who should be in charge? Repository, publisher
- Archival requirements – Long term preservation
  - Why is this important?

#### Why not? EXTRA TIME REQUIRED.

### Solutions:

- make it easier and more efficient – tooling
- funders/institutions to allocate time/cost for this work

Where should tools be made available?

- In the context of a code repository?
  - What are high priority requests for a code hoster like GitHub that would be easy to implement and produce large-scale change?
    - ORCID implementation for seamless author acknowledgement
    - Alternative roles in Github repos, e.g. maintainers, intellectual contributors
    - Discovery: Can Github prioritise CFF files and info for google searches?
- In the context of submission workflows (journal/preprint) that require code deposits?
  - For publishing, the DOI for the _exact_ (archived) version of software used should be cited for reproducibility

CFF specification: [https://citation-file-format.github.io/1.0.3/specifications/](https://citation-file-format.github.io/1.0.3/specifications/)

#### See also:

The policies and guidelines survey done by the Data quality and Curation group:

- [Working document](https://docs.google.com/spreadsheets/d/1HLH1icoT6BT1sj1CifXMStmryitbCOnn8Uxe8Gc6R6c/edit#gid=0)
- [csv file in the repo](/software_best_practices_crosswalk.csv)
