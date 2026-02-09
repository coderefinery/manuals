(contribution)= 
(contribute)=

# Lesson contribution guide

Thank you for taking the time to contribute to **CodeRefinery**! All types of contributions are encouraged and valued. We welcome contributions from everyone (technical experts, legal experts, and newcomers alike). In this document we explain how to contribute to CodeRefinery lessons. The most important takeaways are that i) the barrier for contributiong is low and ii) you can always discuss your proposed small (or huge!) changes with the developers of CodeRefinery lessons.

We use GitHub issues to communicate things that need to be updated, collect feedback and improvement suggestions. 
Latest prior to every workshop we go through the issues and implement and resolve at least the urgent ones. 

All our lesson materials are written in Markdown using fairly normal Sphinx, like how we teach, with a few extras from our own [Sphinx lesson](https://github.com/coderefinery/sphinx-lesson/) extension.


## The broad development process

Our lessons are continually in use as a reference (and sometimes taught by others), but it's OK if they continually evolve.  A few times a year our self-hosted big courses happen: during these times, there is rapid development.  Usually, we try to limit to incremental changes during routine times.  Every so often, there is a period of big updates, where we'll look at all the accumulated bigger suggestions, the current state of the art, and what's needed, plan out a new lesson, and then implement it in time for the next course.  A few lessons each year may get this treatment at most.


## How you can contribute

There are three ways to contribute, ordered from the easiest to the most demanding one:

### 1. Small fixes and suggestions submitted via "Issues"

If you find a typo or have a quick suggestion, but cannot edit it yourself using git, you can open an issue describing the problem or proposal. Maintainers will review your suggestion and address it. 

### 2. Small fixes and suggestions with git

If you are familiar with git version control and you spot a typo, broken link, or error, you can submit a quick fix with git. Even small improvements like clarifying text or adding references are valuable. Usually the process works like this:

* If you do not have one, get a GitHub account. 
* Fork Repository: This creates your own copy where you can freely edit.
* Use the **GitHub's web editor** or your local favourite editor (after git clone) to work on a new version! 
* Make your changes: edit or add the content. Please write in Markdown. If adding code or commands, format them properly (use code blocks) and test if applicable.
* Submit a ***Pull Request***: Once your changes are ready, open a Pull Request (PR) to the main lesson repository. In the PR description, briefly explain your changes and why they improve the lesson. If your contribution closes an existing issue, mention it. CodeRefinery project members will review your PR, provide feedback if needed, and merge it when it’s ready. 

Don't worry about getting the formatting just right.  If you let us know it's not perfect, we can usually quickly fix the synatx.

Tip: If you’re new to this, check out [our lesson on collaborative version control](https://coderefinery.github.io/git-collaborative/).

### 3. Large edits

You can also add substantial contribution to the lessons, like a new section, improve an explanation, or include an example related to a specific topic. For major new content creation, please open an issue first to discuss your idea with the community, so we can coordinate and avoid overlaps.  We can't often make big changes, but we accumulate all the ideas and periodically do big updates.  Please don't feel bad if there is a very long period until a reaction.  Our own ideas get collected the same way.

## Style and content guidelines

To keep the lessons consistent and accessible, please keep these guidelines in mind when writing:

- Clarity and Tone: Aim for a clear, concise writing style. Explain acronyms or technical terms in simple language so that readers from various backgrounds can follow. Our tone is professional, but not overly formal or technical: think of explaining concepts to a colleague who is not an expert in the topic of any CodeRefinery lesson.
- Formatting: Write content in Markdown. Use headings and bullet points to organize information logically (as seen in our existing chapters). Keep paragraphs short (3-5 sentences) for readability. When adding code snippets, use code blocks and include comments if needed for explanation. 
- Target teaching style: Try to keep in mind that different courses remix the materials in different ways.  Don't remove or rearrange lots of material to optimize for one path, instead instructors are expected to pick and choose the episodes (pages) they want to teach.  These bigger arrangements happen during the major development sessions.  (The threshold for adding a new episode isn't so large, if it's an optional episode.)
- Length: beware of adding too much and increasing the length.  There is always more to add, but there is also a strict time limit.  Most lessons are designed to give learners a taste of the material and be able to do follow up reading.
- Content Accuracy: Ensure any facts or claims are accurate, ideally with a peer reviewed citation. 
- Originality and Licensing: Contribute only your own work and do not plagiarize from other texts. By submitting a contribution, you agree that you wrote the content (or have rights to it) and that it can be included under the project’s open license.
- Privacy Considerations: Your name (or nickname) will be publicly visible and associated to the contribution. Due to the distributed nature of open source projects, you accept that it will be impossible to delete your contribution from the version control history.
- Use of generative AI: the use of generative AI is accepted only for basic checks of grammar, spelling, and punctuation. If you use generative AI you must declare it in your contribution and describe how it was used. 
- Images: only original images can be submitted. Image files for new images should be submitted as editable format using SVG as open standard for vector graphics. Photographs can only be used if released with a compatible creative common license. 
- For any contribtion larger than fixing a typo: Do not forget to add yourself as a contributor in the lesson repositories citation.cff file. 

## Lesson preview

Preview lesson page by building it locally using Sphinx, see also [Sphinx-lesson build](https://coderefinery.github.io/sphinx-lesson/building/).

## Creating a new CodeRefinery lesson

We have a self-explaining [Sphinx-lesson](https://coderefinery.github.io/sphinx-lesson/). 

## Code of conduct

Our virtual lesson environment adheres to the [CodeRefinery "Code of Conduct"](https://coderefinery.org/about/code-of-conduct/) to ensure a welcoming environment for all. By participating, you are expected to uphold this code. In short, please be respectful and constructive in your interactions. For example, we expect everyone to be open to different viewpoints, to give and receive feedback kindly, and to avoid derogatory language – in other words, be empathetic and courteous to others. Admins will take actions in case of violations of the code of conduct.


## Additional resources

Also read {ref}`design` and {ref}`review`. 

## Ask for help

If you have questions about the contribution process or run into any problems please contact support@coderefinery.org
You can also just open an issue with your question. We are always happy to help!

Thanks for making it to the end of our contribution guidelines; we look forward to your suggestions!


