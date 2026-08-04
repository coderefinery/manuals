# Making CodeRefinery lessons FAIR

## Ten simple rules for FAIR training material

Following the [Ten simple rules for FAIR training material](https://doi.org/10.1371/journal.pcbi.1007854) we can determine how CodeRefinery lessons are FAIR (Findable, Accessible, Interoperable and Reusable):

### 1. Share

All our lesson materials live on GitHub in public repositories. All lessons use our Sphinx lesson template as basis and are written using markdown.

### 2. Describe properly

All our lesson repositories include a `CITATION.cff` and a `bioschemas.yml` with the lesson metadata. Some fields are still a work in progress. The CITATION.cff file automatically registers in GitHub and provides option for citation information. The bioschemas file is built into the lesson html website without being visible on the page, it can be read by special crawlers and catalogs. See [lesson metadata](lesson-metadata.md) for the full reference on these files.

### 3. Give unique identity

All our lessons have been published on Zenodo in our CodeRefinery community. Every new release in the GitHub lesson repository creates a new version on Zenodo under the same concept ID (ID linking to all versions of an entry). See [releasing a new version](lesson-version.md) for the release process.

### 4. Register online

Every lesson is already indexed in [OpenAIRE](https://support.zenodo.org/help/en-gb/18-general/169-what-is-openaire) automatically, since Zenodo harvests to OpenAIRE and every lesson release is published on Zenodo (see point 3). Crawlers and catalogs can also discover our lessons directly through the `bioschemas.yml` metadata (see [lesson metadata](lesson-metadata.md)), and all our workshop lessons are linked from our website and the workshop event pages. 

### 5. Define access rules

All our lesson materials live in public GitHub repositories. The CodeRefinery team and instructors have maintainer access to these repositories, everyone else can submit issues and pull requests.

### 6. Use interoperable format

All our lesson materials live on GitHub in public repositories. All lessons use our Sphinx lesson template as basis and are written using markdown and built automatically with Sphinx to GitHub pages using GitHub actions on push to main branch. Our documentation lesson teaches how to use Sphinx and how to deploy it using GitHub pages.

### 7. Make reusable for trainers

All our lesson materials are licensed under CC-BY. Everyone can copy, redistribute, remix, transform and build upon the material in any format, giving appropriate credit.

All our lessons also include instructor notes with field reports from previous iterations of teaching, timing estimates and useful teaching related comments.

### 8. Make usable for trainees

Our workshop event page has information on audience, prerequisites and learning objectives. Some lessons have their own learning objectives and prerequisites, but no separate information on the audience.

### 9. Welcome contributions

We generally welcome contributions, especially from people teaching the lessons during our workshop. See our [lesson contribution guide](lesson-contribution.md) for how to contribute; currently this guide lives in our manuals repository rather than in each individual lesson repository.

### 10. Keep materials up to date

We generally update the lesson materials before every workshop together with instructors. We also have [lesson maintainers](lesson-maintainer.md) who keep an eye on each lesson between these updates.

### Additional things we do for our workshop

- Our workshop is streamed live on twitch, everyone can watch, no registration/account required.
- The workshop recordings stay available on twitch for a week after streaming
- We try to archive the recording on YouTube, without breaks, with subtitles and chapters for easier navigation.

## Resources

- Wiegers, L., & van Gelder, C. W. G. (2019). Illustration for "Ten simple rules for making training materials FAIR" (1.0). Zenodo. https://doi.org/10.5281/zenodo.3593258]
