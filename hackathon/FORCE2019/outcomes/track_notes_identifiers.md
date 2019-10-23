**FORCE2019 Research Software Hackathon**

# Identifiers for software track



## Description:

Software is a particular artifact of research that needs to be identified to be cited, referenced and used.

The joint FORCE11 &amp; RDA Software Source Code Identification working group has taken the task of collecting use cases and identifiers schemas that can be used for identifying software.

The following items should be taken into consideration for the identifiers discussion:

   - Granularity of identification

   - Correspondence between different identifier schemas

   - Hacking the software citation graph:

   - Exploring synergies

**Prepared hack and/or documentation:**

- Jupyter notebook for hacking DOI and versions with DataCite&#39;s API: [https://github.com/force11/force11-rda-scidwg/tree/master/hackathon/FORCE2019/hacks](https://github.com/force11/force11-rda-scidwg/tree/master/hackathon/FORCE2019/hacks)
- State of the art document
- [Use cases for identification](https://docs.google.com/document/d/1MTGpwnfMnv3w06sd-m29Ci4cS32X4DlmIapmuQv3tn8/edit?usp=sharing)
- [Software Source Code Identification- State of the art survey](https://forms.gle/97zmT2w3CZUYUqeQ6) form

## Expected outcomes:

- The identifiers discussion can result in a state of the art document which will contain a collection of software identification use cases and software identifier schemas (SCID WG M12 goal).

**Ressources &amp; References:**

- [SCID WG page on RDA](https://www.rd-alliance.org/groups/software-source-code-identification-wg)
- [https://blog.datacite.org/using-jupyter-notebooks-with-graphql-and-the-pid-graph/](https://blog.datacite.org/using-jupyter-notebooks-with-graphql-and-the-pid-graph/)
- [https://support.datacite.org/docs/datacite-graphql-api-guide](https://support.datacite.org/docs/datacite-graphql-api-guide)
- [https://www.pidforum.org/c/pid-graph](https://www.pidforum.org/c/pid-graph)
- Freya- D3.1 Survey of Current PID Services Landscape DOI[10.5281/zenodo.1324295](https://doi.org/10.5281/zenodo.1324295).
- For the[iPres2018](https://ipres2018.org/) conference : Identifiers for Digital Objects: the Case of Software Source Code Preservation [[article](https://hal.archives-ouvertes.fr/hal-01865790v4)][[presentation](https://annex.softwareheritage.org/public/talks/2018/2018-09-25-iPres2018.pdf)]
- In the Datacite blog: DOI Registrations for Software [[post](https://doi.org/10.5438/1nmy-9902)]
- NSRL (NIST)
- SPDX (Linux Foundation)
- SWH-ID (Software Heritage)
- SWID (ISO Standard)
- Wikidata Software Properties
- The ASCL (Astrophysics Source Code Library) registry [[catalog](http://ascl.net/code/all)][[presentation](https://rd-alliance.org/ascl-presentation-asclnet-making-codes-discoverable-20-years)]

**Attendance (n=6)**

| **No** | **Name** | **Affiliation** | **Email** | **discipline(s)** |
| --- | --- | --- | --- | --- |
| 1 | Roberto Di Cosmo | Inria/Software Heritage | roberto@dicosmo.org | Computer Science |
| 2 | Daina Bouquin | Center for Astrophysics | daina.bouquin@cfa.harvard.edu | Astrophysics |
| 3 | Federica Fina | University of St Andrews | ff23@st-andrews.ac.uk | Research Data Management |
| 4 | Peter Chan | Stanford University | pchan3@stanford.edu | Special Collections |
| 5 | Rowan Cockett | SimPEG | rowan.cockett@gmail.com | Geophysics, Software |
| 6 | Morane Gruenpeter | Crossminer/Software Heritage | morane@softwareheritage.org | Computer Science |



## Meeting Notes:

Brief recall of the definition of the Citation Graph: a set of identifiers interconnected through their metadata.

Granularity of identifiers:

We need different levels of identifiers, at least:

- High level identifiers for designating the software project (this can be DOIs/ARKs/Handles/Wikidata ids)
- Low level intrinsic identifiers for a precise version of the software source code (Software Heritage identifiers are the de fact standard for this, and are compatible with git hashes)

Some key issues with high level identifiers schemas (Handles/DOIs/ARKs):

- Ambiguity: same object gets different metadata / identifiers
- Curation: ensuring proper metadata is added
- Intermediaries: there are cases where in the publication process the identifiers get garbled

Side notes on Zenodo:

- It seems that users of Zenodo cannot edit the xml in DataCite directly, and need to go through the Zenodo interface
- Citation recommendations created automatically may be totally bogus, see for example https://zenodo.org/record/1308726#.XaWk6eZKgWN

**Side track on how to archive legacy software**

A rising issue with people retiring and leaving legacy software is how to collect, curate and archive it. A pointer is given to the SWHAP process, that provides guidance for this case: [https://www.softwareheritage.org/swhap](https://www.softwareheritage.org/swhap)



Reference chasing and examples on the different aliases used for software citation: https://github.com/dbouquin/cite\_astro\_software\_2019/blob/master/XML\_SEARCH/XML\_ALIAS\_LIST.txt

Issuing DOI

Scholix project- [http://www.scholix.org/](http://www.scholix.org/) harvest all links

Fork example.

To see the evolution of the software.

[**https://github.com/chrislgarry/Apollo-11/issues/426**](https://github.com/chrislgarry/Apollo-11/issues/426)

Use cases:

- Check the article of the software references to see if it is compliant with a software identification policy
  - Example paper with lots of citations to software: [https://arxiv.org/pdf/1901.00143.pdf](https://arxiv.org/pdf/1901.00143.pdf)
  - Accessible online
  - Using the github link or the github-zenodo integration for the DOI.
- Build the relational graph- connecting records, between repositories
  - What do you want to link? Not necessarily citation
    - To the repository for reuse
    - To the manual
    - To the dependencies - Where should I put the metadata about identifying the dependencies?
    - To the authors pages- github handle/ORCID
    - To the hardware
- Build the PID citation graph
  - [https://blog.datacite.org/introducing-the-pid-graph/](https://blog.datacite.org/introducing-the-pid-graph/)

[ANNOTATION:BY &#39;Daina Bouquin&#39;
ON &#39;2019-10-15T11:20:57&#39;
NOTE: &#39;**Already complete https://codemeta.github.io/crosswalk/wikidata/**]
Crosswalking identifiers using Wikidata (SPARQL)
- Preserve the metadata with the PID to the archived version of the software
- Computer art- linking between artifacts sequentially to have the same experience



Crosswalk identifiers use cases and schemes:

- Working document: [https://docs.google.com/spreadsheets/d/17YzqH1W1MnrWAC7WJZGaX\_0jCczTuUJlI7UfhyJ4lwY/edit?usp=sharing](https://docs.google.com/spreadsheets/d/17YzqH1W1MnrWAC7WJZGaX_0jCczTuUJlI7UfhyJ4lwY/edit?usp=sharing)
- [First Draft](outcomes/crosswalk_identifiers.csv)
