(review)=

# Lesson review checklist

This presents a checklist for reviewing lessons that already exist.
You should also read [lesson-design.md](lesson-design.md) as well -
this is roughly a checklist to the things there.

Remember to keep the *story* of the lesson in mind.  Many people are
focusing on the small matters (during every change), but only
occasionally do people look at the big pictures.  That's why a proper
review starts with looking at the big picture, instead of adjusting
small things and possibly derailing the story.

This is roughly sorted from highest priority for short review to
lowest priority for big refactorings.


## Issues

- Look through the issue tracker to see what is relevant, remember and
  follow up when going through the sections below.


## Lesson guides

Instructor's guide:

- What sections should be taught for what audiences?
- Common pitfalls when teaching
- Any required setup in advance?
  - Any special config files that need to be cleared on instructor's
    computer when teaching?

Maintainer's guide:

- Learning objectives (necessary to know its place)
- Learner personas (necessary to know its place)
- After you're done analyzing, is there anything in the maintainer's
  guide you need to update?  (The maintainer's guide is probably in
  most cases the same as the instructor's guide)
  - Design philosophy, how to modify while preserving the overall
    character.

Student reference guide:

- Anything to fix or already?
- Keep this in mind when you get to episode details.


## Lesson overview

- Is the introduction intrinsically motivating enough?  Does it
  promote an emotional connection to existing problems?
- Student's guide and framing: will a student know when this is
  relevant to them and how it will benefit them?
  - Doesn't need to include word-for-word learner personas, but should
    convey this somehow.
- Are the difficulty and prerequisites stated?


## Episode overview

- Read the intro and conclusion to every section/episode.
  - Do they make sense when you read them in order, without reading
    the text in between?
  - Do they motivate each section well enough (not just explain what,
    but why it's cool?)
- Do they have learning objectives at top and food for thought at the
  bottom?
- Are optional or advanced episodes marked as such?
- Does the episode (or lesson overall) say what is next, to keep
  people interested in growth?


## Episode details

- Read through each exercise (with no other text in between).  Does it
  make a logical progression?
- Exercises labeled with difficulty, optional, etc.
- Optional advanced exercises or material in places where advanced
  users may get far ahead.
- Each exercise is self-contained: a helper can read just the exercise
  area and get an idea of what is supposed to happen and why.
- Update the student's reference guide as you are going through the
  details.
- Remove duplicate or unnecessary information when possible.  Things
  are always added, rarely removed.  Shorter is usually better.  If
  something shouldn't be removed, perhaps mark it as advanced or
  optional.


## Major Refactorings

Major restructrings should be rare and usually happen as agreed in a
group.

Always start with the big picture: does it make sense?  When
refactoring, always start off with backwards lesson design again (see
lesson-design.md) and fully go through that.

After the above, do the details.  Remember the guides still.

Before you start major refactoring and rewriting, think if it makes
sense.  Have you figured out why it's the way it is based on the
instructor's guide?  If you do a big refactoring, make sure you update
the maintainer's guide!

Before you embark on a big refactoring step, please pitch your idea
in a GitHub issue and collect feedback from others.  Maybe even hold a
brainstorming session.
