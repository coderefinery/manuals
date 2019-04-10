# Lesson design

This is a checklist and hints when writing and designing a new lesson.
The master material is in Teaching Tech Together, primarily chapters 6
and 12 for practicalities and 2 and 4 for big picture considerations.
But really, all the book.  See [the summary we
made](teaching-tech-together.md) or [the actual
book](http://teachtogether.tech/).


## Backwards lesson design

Think test-driven development: decide what you want students to be able
to do, design exercises to measure it, then fill in the gaps with
teaching.  You can see [their
summary](http://teachtogether.tech/en/template/).  The steps are:

1. Brainstorm what you want to cover
2. Create or reuse learner personas
3. Create formative assessments (exercises) that let the learners
   practice what you want them to learn.  See below for hints on coming
   up with good exercises.  The exercises (at least some) should try
   to connect to things that learners will actually do.
4. Put exercises in a logical order, and fill in any gaps.  Ideally
   there should be 15-20 min of teaching between each.  Not every one
   has to be very long
5. Write just enough material to get from one exercise to the other.

Most importantly, start from tech details, start from learner's needs
and how they can feel connected.


## Emotional and intrinsic appeal, other basics

You can think of why people should feel emotionally connected to your
material - maybe it's too much to expect people to get emotionally
invested, but if you try for that, you'll end somewhere better.

Try to design around tasks and exercises which your audience will care
about.  For example, don't say "here are some shell commands", but
"the shell helps you to do your work more efficiently... once you know
it, you will really feel at home.  Here are some typical things you might
do."

A manual is reference, a tutorial builds a cognitive model.  If you
can build the cognitive model, tell them the "why", students may be
able to refer to the manuals themselves.  Teaching should be more
tutorial, with good links to manuals (it can also explicitly teach
how to use the manuals).


## Planning

- Do some planning, and *document it* - the design process helps
  others to teach and modify.  At least put it in the README.  (this
  is the **designer/maintainer's guide**)
- Make learner personas: what is your target audience?
- Decide learning objectives based on the personas: high-level end
  goals.  What students get out, not what they do.
- Also make a *guide* for teaching (**instructor's guide**), "if you
  want to present this, do this".
  - How much preparation is needed?  Is it enough to know the topic
    and have read the material?
  - Things to prepare before the presentation.  Does anything need to
    be set up?
  - Practical notes on presenting.
  - Are there solutions to exercises somewhere?  Are they needed?u
  - Include some pre-assessment questions which can be asked at the
    beginning.
  - Perhaps you should do this at the end, but at least starting the
    instructor's guide at the beginning will frame your writing.


## Writing

Not much here yet, mostly just follow the "backwards lesson design"
above.  The hardest part is coming up with good exercises, so our
practical advice is to mix and max from the two taxonomies at the
bottom and the exercise types.  Try to think of diverse types of
exercises.

- Make sure you include the emotional starting point at the top - why
  should you care and why is this cool?
- This should also be at the start and end of each section: not what
  or how, but why?
- Part of this is also having a **student's guide**, so that
  people independently studying can know how to follow the material.
- It's OK to have more material than can be presented or than people
  should know, but *label things well*, including *labeling the difficulty*.
  - In the beginning, what sections are expected to be taught in
    short/long versions?  What's advanced/optional?
  - Label advanced and optional sections as such.  Perhaps also really
    basic sections that can be skipped for that reason.

Plan for mixed abilities.  It's OK to have optional (basic) and
advanced sections, as long as they are clearly labeled.

Once you are done, update maintainer's and instructor's guides.

## Exercise types

The main point of different exercises types is to have some which have
lower cognitive load than just "do it from scratch yourself".

One of your other primary goals should be to make your exercises
*relevant*.  Abstract will lead to disconnection, but if they relate
to the real world.  Also, can you tell a complete story with
exercises?


Basic:
- Multiple choice (easy to get feedback via a classroom tool)
- Code yourself (traditional programming)
- Code yourself + multiple choice to see what the answer is (allows
  you to get feedback)
- Inverted coding (given code, have to debug)
- Parsons problems (working solution but lines in random order,
  learner must only put in proper order)
- Fill in the blank

More advanced:
- Tracing execution
- Tracing values through code flow (e.g. what is the sequence of
  values that `x` takes on?)
- Reverse execution (find input that gives an output)
- Minimal fix (given broken code, make it work)
- Theme and variations (working code, adapt to other type of
  situation/problem)
- Refactoring

More conceptual:
- Draw a diagram
- Label diagram
- Matching problem: two sets of Q/A, match them.


## Reference material
- Bloom's taxonomy: hierarchical skill levels
  - Remembering
  - Understanding
  - Applying
  - Analyzing
  - Evaluating
  - Creating
- Fink's taxonomy: complementary types instead of hierarchical:
  - Foundational knowledge
  - Applications
  - Integration
  - Human dimension
  - Caring
  - Learning how to learn


## Reviewing existing lessons
Are you trying to improve/maintain a lesson that already exists?
This section is for you.

Always start with the big picture: does it make sense?

- Instructor's guide (see topics above)
  - What sections should be taught for what audiences
  - Common pitfalls
- Student's guide and framing.
- Exercises labeled with difficulty, optional, etc.
- Are the intros emotionally motivating enough?
- Read the intro and conclusion to every section/episode.
  - Do they make sense in order?
  - Are they motivating/wrapping up well enough?
- After you're done analyzing, is there anything in the maintainer's
  guide you need to update?

After the above, do the details.  Remember the guides still.

Before you start major refactoring and rewriting, think if it makes
sense.  Have you figured out why it's the way it is based on the
instructor's guide?  If you do a big refactoring, make sure you update
the maintainer's guide!
