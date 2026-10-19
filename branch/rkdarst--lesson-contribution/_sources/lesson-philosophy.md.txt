# Lesson philosophy

This page describes the overall spirit of how our lessons are made -
basically, what to think about when designing or improving a lesson.
Other pages go into details about how this is implemented.


Terminology:

Lesson
	One repository containing a package of teaching material, for
	example git-intro.  For courses with all material in one
	repository, "lesson" could also mean one episode there.

Episode
	One page within a lesson.

Workshop or course
	One instance of giving one or several lessons.


## Summary

CodeRefinery lessons are designed to be widely applicable lessons for
the beginner to intermediate level, designed to get people started on
a path so that they can continue learning themselves.  They are
designed to have a few practical things and exercises that can be
actually be done, but almost everyone will need to continue their
learning after the lesson is done to put things into practice.

Lessons focus on both the overall motivation and "quick wins" at the
beginning, and the later parts usually have a demonstration of more
advanced follow-up ideas that need self-study.

Lessons are designed to be practical for learners who need to
computing, but aren't "computing people".  This means we make plenty
of compromises for simplicity that are not what instructors would do
themselves on a daily basis.


## The target audience

CodeRefinery is mainly focused on people who are already doing some
sort of scientific or research (or other real-world) work, but haven't
been introduced to the best computational practices.  Thus, we are in
an interesting place:

* Our audience isn't pure beginners, since people are in practice
  working already.  Many may be beginners to the actual topic, but
  many will have seen bits and pieces through their work.

* Our audience probably is not advanced in the topics we teach, since
  we focus on introducing learners to new topics.

Our audience is also very diverse - not just demographically, but what
they study and how they will actually need to use computing in the
future.  Taken together, this means that lessons and instructors need
to do a lot of work explaining what is relevant to which parts of the
audience.


## Learning pathways

In general, we tend to teach widely applicable basics, with the
expectation that our learners are smart and will be able to follow up
and continue learning the details they need later on (which will be
different for each person).

Modern learning is much different than before.  Decades ago, courses
and information were harder to find, so people would attend courses
for long-term knowledge.  These days, information is at our fingertips
and we expect to find what we need, just when we need it.  And there
is so much to possibly know (and it's hard to know just what is
relevant at any time).  Thus, long courses are a hard sell.

Self-study materials and AI is able to answer many questions without
having done long study - but still, some background is needed to be
able to find the right material and ask the right questions, since
there are just so many possible ways to do any given task.

This leads to the overall philosophy of: **broad introduction to a
topic with various follow-ups suggested both within the lesson
(advanced material not covered in the main flow) and what to learn
next.**


## Design choices

The above leads to various philosophical design choices:

* The main lesson flow is designed around beginners in the topic but
  people already in "research life".  This means that learners want to
  get to some point and many won't want to study the material
  excessively just for its sake.  On the other hand, learners have
  experience doing new things so if you give them the right
  foundation, they can figure stuff out.

* There is a significant focus on practical exercises, not just
  theory.

* There is often advanced and optional material within lessons which
  isn't taught.

* There is not one fixed flow.  Instructors may teach different
  episodes in different courses without changing the actual material,
  though the first few episodes are often fixed.  Learners may attend
  different lessons.

* They are designed to balance the needs of in-person teaching, online
  teaching, and self-study.

* They are not pedantic and realize that beginners have different
  needs than experts than teachers (while trying to give the idea of
  these better ways of working).


## But not just this

CodeRefinery is growing into not just one single workshop program with
some lessons, but a network of people teaching different courses.
There's nothing wrong with adapting this philosophy to fit your use
case, whether the course is more advanced or for a more focused
audience.  If you do that, the ideas on this page may help you explain
the target audience of your particular lesson and how it compares to
others.
