# Lesson credits

To acknowledge all contributors to our material we have implemented `CITATION.cff` files to all our lesson repositories in 2025. See [lesson metadata](lesson-metadata.md) for the full reference on what's in these files and when they get updated.

We've decided not to distinguish different levels of contribution: everyone who contributed more than a typo fix is listed as an author, if they wish so. 

In 2026 we also added bioschemas.yml, which in addition to author, also introduces a contributor field. We keep everyone as author in both files rather than splitting across the two.

In 2026 we also started with a more formal role of lesson maintainer. The current maintainer(s) are recorded in the `contact` field of `CITATION.cff`, and are also named in the README. See [lesson metadata](lesson-metadata.md#lesson-maintainer-metadata) for how this carries through to bioschemas.yml and Zenodo.

## Adding an author

If you have been linked here, you might have been asked if you want to
be listed as an author.  If someone has asked you, then don't worry if
you contribution is enough: the threshold is not high.  If so,
consider:
- Your name and info will be included in the Zenodo citation, which is
  permanent
- You will be included in future releases as well, unless you ask to be removed
- Please send us: family-names, given-names, and if you want ORCID
  ([reference of valid
  keys](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md#definitionsperson)).

The preferred way is to open a pull request adding yourself directly to
`CITATION.cff`, under the `authors:` list, for example:

```yaml
authors:
  - family-names: Doe
    given-names: Jane
    orcid: "https://orcid.org/0000-0000-0000-0000"
```

New authors are usually appended at the end of the list; there is no
strict ordering requirement. If you'd rather not deal with git/YAML,
send us the same information and a [lesson maintainer](lesson-maintainer.md)
will add it for you.

Maintainers should be proactive reach out to people when they contribute,
but everyone should also send a pull request to be included in
CITATION.cff if you desire.  Note that not all contributions may be visible from the Git history. Often, multiple people are involved in change discussions. Those should at least be asked if they want to be named as author.

Regenerating `bioschemas.yml` from `CITATION.cff` happens as part of
[releasing a new version](lesson-version.md), so it doesn't need to be
done manually when adding an author.


## Adding an acknowledgee

There are very many, so we try to add them to the lesson
README page if it's not based on a Github interaction (or if it's desired for
some other reason).




