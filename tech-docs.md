# Writing technical docs

This is a guideline for non-teaching technical documentation, for
example HPC infra usage.  Since many of us overlap with HPC or other
support roles and our CodeRefinery mindset partially overlaps, we have
some brief guidelines here.

There is far too much professional information for us to reproduce
here, but hopefully this is useful quick reference for a typical
person to get started.  Check the links at the bottom for more.



## What kind of doc?

* **Tutorial** - emphasis on concepts and mental model, after reading
  you can do limited things.

* **Reference** - more likely to read if you know the concepts and
  want to know more advanced stuff.

* **Example** - example of one specific thing.  Good for copying and
  pasting if you know enough to understand it.

"A good tutorial is different from a good reference.  Very few things
are good at both at the same time." - (I don't remember who, seen in
Teaching Tech Together).  Thus, both tutorials and reference are
useful.  Sometimes, we need a tutorial for our stuff and can point to
outside material as a reference.  People also really want examples
they can copy - is your infra similar enough that outside examples can
be copied?



## Recommended sections/things to include

(Of course, depending on what type of doc it is)

* Introduction that says *when* this material is relevant and *why*
  you might want to use it.  (*who* it is written for, *when* it was
  updated).  Prerequisites.

* If relevant, there is a *concepts* section at the beginning.
  Perhaps define a few key terms.  Possible prerequisites (required or
  possibly useful).

* Is the actual *content* good and understandable?  Are any conceptual
  or technical prerequisites mentioned in the introduction (or when
  they are needed, if minor)?

* *Examples* spread throughout.

* A *conclusion* that wraps up and what happened, why, and what comes next.

* "*See also*" section at the end if relevant.

* If relevant, *exercises* at the end or spread throughout.  Even if
  this isn't the point, it makes people think and makes it minimally
  useful for informal teaching.


## Style suggestions

(not standards, since of course people do what they want anyway.  Not
all things apply in all cases)

* **Bold** for definitions or the first time a concept is introduced.
  Basically, a time where someone is likely to scan up the document to
  remember what a certain concept is, such as "what's a git stash?"

* *Italics* for local emphasis.

* Never feel bad to use simpler text, in the best case someone can
  now understand, in the worst case there's less mental effort.

* Use an active/imperative voice (Y does X, do X to get Y), not
  passive (X can be done by Y).  Try to use present tense.

* Make the docs skimmable - by looking at headings and first words in
  each section, can you figure out what you need to focus on?

* Use gender neutral text, of course.


## Style guide

(Is it worth making a minimal academic HPC/tech doc style guide?  The
benefit would be that we can share stuff better.  There's no need to
emulate or reproduce actual professional ones, since we probably
aren't that formal.)


## Other ideas

Consider documentation-driven development.  Write basic docs, review,
then implement it.


## See also

Of course, there is far more professional information than you can
find above.

* The [Write the Docs](https://www.writethedocs.org/guide/) guide
  seems useful - especially about organizational aspects.

  * [Principles](https://www.writethedocs.org/guide/writing/docs-principles/)

  * [Styles and list of style
    guides](https://www.writethedocs.org/guide/writing/style-guides/),
    though most are probably too long for hobbyist reference.

* [lesson-design.md](lesson-design.md) might be useful to understand.
  The "backwards lesson design process" is especially important to
  think about: while you don't have exercises, you do have goals to
  accomplish you can design to.
