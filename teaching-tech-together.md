# Summary of Teaching Tech Together

[Teaching Tech Together](http://teachtogether.tech/) is a book
compiled by Greg Wilson which is about the pedagogy and practical
hints of teaching technology in informal environments.  It is a very
good resource, and the main point is that research does back up
teaching, it's not all intuition.  Many citations are included.

This page contains a summary of the most important points.  The point
is that one can quickly refer to this before writing a new lesson or
teaching a course.  The article [Ten quick tips for creating an
effective lesson](https://doi.org/10.1371/journal.pcbi.1006915) is
also a good summary of the main lesson design points of this book.

Useful appendices:
* [Backwards lesson design
  template](http://teachtogether.tech/en/template/)
* [Checklist for events](http://teachtogether.tech/en/events/)


## Ch1: Introduction
* **Novice = no good mental model of what they are learning**, "not even
  wrong"
* A manual is *not equal* to a tutorial - a tutorial needs to build a
  mental model from scratch.
* Formative assessment = determine what the misconceptions are.


## Ch2: Building mental models
* "Expert blind spot" = experts have more links, so don't see what
  links are missing.
* Concept maps as a metaphor for connections
* 7+/-2 concepts can fit in short term memory at once
* Get feedback from others, then give feedback to others, then
  self-feedback (last one is "deliberate practice")


## Ch3: Expertise and memory
* Cognitive load: too much is bad and makes learning slow
* **Faded example**: blank out certain things in an example which are
  added as an exercise/example (what you want to progressively
  teach).  Seeing examples is good, debugging as an example.
* "I want to do something, not learn how to do everything"
* **Parsons problems** - give working code but in random order,
  students must put it into the right order.
* Minimal manual: one page micromanuals on specific tasks.  Helps
  training but loses content.
* The last exercise of this chapter has some good hints for making
  useful graphics.


## Ch4: Cognitive load
* Cognitive load is divided into intrinsic load (background required
  learn), germane load (mental effort to link new to old), and
  extraneous load (everything else that distracts from learning).
  (this is "cognitive load theory")
* A paper claimed that self-guided learning is less effective, because
  people are overloaded: you have to both learn new facts and learn
  how to use them at the same time.
* Strategies: use exercises well that minimize tho load.  a) parsons
  problems, b) labeled subgoals, c) split attention (separate
  channels, but complimentary rather than redundant), d) minimal
  manuals

## Ch5: Individual learning
(chapter about how people can help themselves)
* Six strategies: a) spaced practice, b) retrieval practice, c)
  interleaving (abcbac better than aabbcc), d) elaboration (explain to
  self), e) concrete examples, f) dual coding (e.g. words and
  pictures, or different forms of same material).
* Manage time well
* Peer assessment

## Ch6: A lesson design process
* Backwards lesson design, similar to test-driven development: 1)
  brainstorm ideas for what to cover, 2) create learner personas to
  figure out who you want to teach, 3) create formative assessments to
  give learners a chance to exercise what they are trying to learn
  (3-4 per hour), 4) put formative exercises in order, 5) write the
  teaching material around this.
* Learner persons, to guide your design process: a) general
  background, b) what they already know, c) what they *think* they
  want to know, d) how course will help, e) special needs.
* Learning objectives: write objectives and think of what depth of
  understanding you are getting too.  Consider Bloom's taxonomy: a)
  remember, b) understand, c) apply, d) analyze, e) evaluate, f)
  create.
* Fink's taxonomy (unlike Bloom's, complimentary not hierarchical): a)
  foundational knowledge, b) application, c) integration, d) human
  dimension, e) caring, f) learning how to learn.
* Maintainability: is it easier to update than replace?  a) **You have to
  document the lesson design process**, b) technical collaboration, c)
  are people willing to collaborate?  Or do teachers resample rather
  than update?

## Ch7: Actionable approximations of the truth
(chapter about learning programming specifically... title comes from
not necessarily having clear research that says what you *should* do,
but you have to do something anyway)
* Experts know *what* and *how*, novices lack both but most teachers
  focus on *what* only.
* Think about teaching debugging and using it as examples - the *how*.
* If you are teaching programming specifically, just [read the
  chapter](http://teachtogether.tech/en/pck/).


## Ch8: Teaching as performance art
* Get feedback on your teaching.  People aren't born teachers, and
  feedback isn't in the western teaching culture enough.
* Use live coding.  It's much more effective, especially because it's
  two way and *you can demonstrate making mistakes*.  a) embrace your
  mistakes, b) ask for predictions, c) take it slow, d) be seen and
  heard (stand + microphone), e) mirror your learner's environment, f)
  use the screen wisely (make it big enough), g) double devices (one
  to present, one for notes), h) use diagrams, i) avoid distractions,
  j) improvise after you know the material, k) face the screen only
  occasionally
* Drawbacks of live coding, which you can minimize over time: a) going
  too slow, b) exercises can be too deep and have too much cognitive
  load (give skeleton code).


## Ch9: In the classroom
* Code of conduct: teaching isn't for those that are already "in",
  it's for those that aren't.  If you don't notice problems and
  enforce it transparently, it means nothing though.
* Peer instruction.  Discuss in groups.  e.g. multiple choice
  question, if there is a wide variety of wrong answers, have them
  discuss in groups.
* Teach teaching: different strategies, consider what you want to do:
  a) teach teaching (taking turns) b) teach and assist (going around
  helping) c) alternative teaching (group with more specialized
  instruction), d) teacher and observer, e) parallel teaching (two
  groups, same material), f) station teaching (rotate through
  stations).
* If co-teaching, plan ahead: a) confirm roles at start, b) work out
  some hand signals for common conditions, c) each person should talk
  at least 10-15 min at a time, d) person who isn't teaching shouldn't
  distract, though leading questions OK, e) check what your partner
  will teach after you are done, f) inactive teacher stays engaged,
  not doing own stuff.
* Plan for mixed abilities, especially false beginners who have
  studied the material before.
* Can you make a collaborative not online document?
* Sticky notes
* Don't start from blank pages, give some starting point.
Many other good points in [the chapter
itself](http://teachtogether.tech/en/classroom/).


## Ch10: Motivation and demotivation
* Extrinsic vs intrinsic motivation.  Extrinsic: have to do it for job
  or something.  Intrinsic: do it for self, you want to encourage
  intrinsic motivation.  Drivers of intrinsic motivation: a)
  competence, b) autonomy, c) relatedness (connection to others).
* Consider usefulness and time to master.  Focus on useful and fast.
  Useful = *authentic tasks*, things people will actually use.
* Avoid demotivation: for adults, a) unpredictability, b)
  indifference, c) unfairness.  Specific examples: a) contemptuous
  attitude, b) saying existing skills are worthless, c) complex or
  detailed technical discussion, d) pretending you know more than
  they do, e) the word "just" as in, it's "just easy", f) software
  installation problems, g) giving impossible challenges to fail at to
  try to learn something, if not understanding.
* Consider accessibility and inclusivity - consider things are harder
  for others, try to understand diversity of backgrounds.

## Ch11: Teaching online
* Disadvantage of MOOCs: can't clear up individual misconceptions
* The chapter has various good ideas, including how to make sure
  everyone is heard (certain group doesn't dominate online
  discussions), short cycles and short exercises, require some small
  group work, use videos to engage rather than instruct (people can
  read faster), identify and clear up misconceptions early.
* Flipped classroom: watch lectures on own time, do exercises and
  discuss in class time.

## Ch12: Exercise types
* Multiple choice, code yourself, code+multiple choice, inverted
  coding (given code, test and debug), fill in the blanks, Parsons
  problems (given questions but in wrong order).
* Tracing execution, tracing values, reverse execution (find input for
  output), minimal fix, theme and variations, refactoring exercise.
  Pen and paper exercises.
* Diagrams and connection: draw diagram, label diagram, matching
  problems.
* Autograding is hard, in particular most automatic grading tools
  don't provide useful feedback messages.  Also, automatic grading can
  only test low-level skills, not higher abstractions like code
  review.

## Ch13: Building community
(Chapter about forming a community of teachers and learners working
together)


## Ch14: Marketing
* Think about what you are offering to who.  Who are the target
  audiences and why should they be care and become invested?


## Ch15: Partnerships
* Main two points are work within schools or outside of schools.  If
  inside, part of academic programs?  Academic programs and especially
  teachers change very slowly.


## Ch16: Why I teach
([A note from the author](http://teachtogether.tech/en/finale/))
