(review)=

# Lesson review checklist

This presents a checklist for reviewing lessons that already exist.
You might want to also read [lesson-design.md](lesson-design.md) as
well - it shows the picture of big redesigns and making of new
lessons.

When reviewing lessons before teaching, the main thing to keep in mind
is: you don't need to change a lot!  The lessons mostly work, and need
some updating.  But, you shouldn't look at it as too big a job.  Try
to keep the working things and make the needed changes.  Save big
changes for less frequent rounds of improvement.

This is roughly sorted from highest priority for short review to
lowest priority for big refactorings.

## What you should focus on

When reviewing/updating a lesson to teach, focus on:

- Do exercises and demos still work?
- Any small-scale clarifications to make things flow better?
- Does the "big story" need more clarifications?
- Using the plan from previous years, with improvements.

Try to avoid:

- Changing the whole design of the lesson (unless you are doing a big
  improvement round - discuss in a meeting to set the plan)
- Removing stuff you won't teach (other people may use that in their
  flows.  It may be taught later)
- Changing text too much to optimize for only one path (it should be
  reasonably modular, so that teachers can pick and choose)
- Explicitly changing exercises to demos, or demos to exercises (it
  can be taught both ways.  Try to make it suitable for both.)


## Look at reports from previous years

- There are reports maybe in the instructor's guides or an issue.
  - They should hopefully say timings and what went well or not.
- Check the notes archive from previous workshop - the questions that
  were asked for the session, and the feedback of the day.


## Issues

- Look through the issue tracker to see what is relevant, remember and
  follow up when going through the sections below.
- Remember to add your own issues about how it went after you teach!


## Lesson guides

Lessons should have some guides for instructors/maintainers.  They may
be more or less up to date, but it's the first thing you should read.
(Maybe you want to update these after teaching...)

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


## Run through the whole lesson

- Run through the parts you will teach.  Do all the examples by
  yourself.



## Exercises and demos, episode details

Most of your review time should be focused here.

- Read through each exercise (with no other text in between).  Does it
  make a logical progression?
- Exercises labeled with difficulty, optional, etc.
- Optional advanced exercises or material in places where advanced
  users may get far ahead.
- Each exercise is self-contained as much as possible (not every one
  can be): a helper can read just the exercise area and get an idea of
  what is supposed to happen and why.
- Update the student's reference guide as you are going through the
  details.
- Remove duplicate or unnecessary information when possible.  Usually,
  things are added and not removed.  This leads to a lot of excess
  material.  Shorter is usually better.  If something shouldn't be
  removed, perhaps mark it as advanced or optional.
- Exercises vs demos
  - Things should be marked "demo" if it would be hard for a learner to
    do it themselves.
  - Things should be marked "exercise" if it should have everything
    necessary for a learner to do themselves.
  - Exercises can always be done as demo if the teacher decides
    (regardless of what the lesson says).



## Episode overview

Verify each individual episode has a overall motivating story (why,
what, why, what's next):

- Read the intro and conclusion to every section/episode.
  - Do they make sense when you read them in order, without reading
    the text in between?
  - Do they motivate each section well enough (not just explain what,
    but why it's cool?)
- Do they have learning objectives at top and food for thought at the
  bottom?
- Does the episode (or lesson overall) say what is next, to keep
  people interested in growth?



## Lesson overview

Verify the lesson overall picture is motivating and forms a complete
story (why, what, why, what's next):

- Is the introduction intrinsically motivating enough?  Does it
  promote an emotional connection to existing problems?
- Student's guide and framing: will a student know when this is
  relevant to them and how it will benefit them?
  - Doesn't need to include word-for-word learner personas, but should
    convey this somehow.
- Are the difficulty and prerequisites stated?
- Does the wrap-up tell what was learned?
- Does it tell why it was learned?
- Does it tell what learners should do next?


## Installation instructions

- Verify everything works with the standard CodeRefinery environment:
  <https://coderefinery.github.io/installation/> (not your own
  personal environments: learners won't use that)
- Propose updates to the install instructions as needed.



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
