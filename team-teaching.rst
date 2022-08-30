Team teaching
=============

Listening to only one person talk can be boring.  Listening to a discussion is
much less so.  "Team teaching" can mean many things, but in this case we
are referring to **two instructors are both actively
involved in lecturing at the same time**, as some sort of conversation
between them.  It is a form of co-teaching.

When it works well, it makes a lecture much more dynamic and
engaging, and reduces the load for each person to plan everything
because you can rely on two minds to do it live.
The difficulty is that you need to coordinate and it is our nature to
keep talking while teaching, making a conversation difficult.

.. seealso::

   `Demo of CodeRefinery livestream teaching
   <https://www.youtube.com/watch?v=WjmttAniZX8>`__.  This shows a
   demo of many parts of team teaching on a livestream - read the
   video description for details.



Basics
------

.. figure:: img/teach-teaching--screenshot.png
   :align: right
   :figwidth: 50%

   Demo of team teaching.  Two people are speaking, in this case one
   is typing and giving the small point of view, and one is explaining
   the big point of view.


We can't claim to know the best way to do this yet, but we have seen ways
that work and don't work.

The basic idea is that you want to keep a constant *conversation*
going.  This can be a mutual discussion, one person explaining big
concepts and one the details, one person asking
questions and the other answering, or some other combination.  *This
is different that two people teaching different sections.*

There is less need for the instructors to prepare every single thing,
since you can rely
on the wisdom of the group to get you through areas you haven't
perfectly prepared.  In fact, this is good, because then your learners will
see things go slightly wrong and your live debugging.
Still it can be useful to agree with your co-instructor on the choreography
of your session (more about this below).

| One of the most important principles of ship handling is that there
| be no ambiguity as to who is controlling the movements of the
| ship. One person gives orders to the ship's engine, rudder, lines,
| and ground tackle. This person is said to have the "conn."
|
| — James Alden Barber, 2005, "Introduction", The Naval
| Shiphandler's Guide, p. 8. Mark B. Templeton, via `wikipedia <https://en.wikipedia.org/wiki/Conn_(nautical)>`__

As the quote says, in any large enough operation, multiple people are
involved, but responsibilities should be clear.  At least, the team
should know who is pushing things forward (even if, to make it seem
live, they still discuss among each other anyway).

We propose two basic models, but of course there is a constant
continuum.
And in either model it can be good to switch roles every 20-30 minutes.



Model 1: Guide and demo-giver
-----------------------------

One person serves the role of **guide**, explaining the big picture
and possibly even the examples.  The **demo-giver** shows the typing
and does the examples, and could take the role of a learner who is
asking about what is going on, the person who actually explains the
details, or an occasional commenter.  Anyway, the guide is the one
navigating through the course and bringing up material in a logical
order for the audience and "has the conn".

Hands-on demos and exercises work especially well like this.  Here,
the guide would follow the outline and serve as the director (see
below).

.. csv-table::
   :delim: |
   :header-rows: 1

   Guide                      | Demo-giver
   Introduces most material   |
   Goes through theory        | Asks questions that a learner may ask
   Introduces type-along      |
   Explains steps of type-along | Types during type-along
   Asks questions to Demo-giver during type-along | Explains details what they are typing and what happens
   Looks at HackMD during type-along  |  Looks at HackMD during theory
   Discusses during Q&A       | Discusses during Q&A



Model 2: Presenter and interviewer
-----------------------------------

In this case, it is the **presenter** who is mostly explaining *and*
giving the demos, and generally trying to move the forward through the
material.  The **interviewer** serves as a learner or spotter, fills
in gaps by asking relevant questions, and tries to comment to the
presenter when things are going off track.  The interviewer "has the
conn".

This is closer to normal teaching, so feels more natural to do.  The
big disadvantage is that it's the tendency of the presenter to keep
talking, and the tendency of the interviewer to be nice and not
interrupt.  This negates most of the benefit you would hope to have,
but is much better than solo teaching.

Here, the presenter would follow the outline and serve as the
director (see below).

.. csv-table::
   :delim: |
   :header-rows: 1

   Presenter                  | Interviewer
                              | Asks questions to presenter
   Answers questions using their special knowledge | Follows up with learner questions
                              | Pushes forward though the material
                              | Asks questions that a learner may ask
                              | Introduces type-along
   Explains type-along and material | Explains type-along and material
   Looks at HackMD when possible | Looks at HackMD most of the time
   Discusses during Q&A       | Discusses during Q&A



Hints
-----

With more than one person, there is a risk of seeming uncoordinated
when the team doesn't know who is supposed to move the lesson forward.
It's not bad to have short discussions to decide what to do next, it
makes the show seem interactive.  But if it happens too
much, it becomes noticeable.  As quoted above, you could adopt a
principle which exists
in many domains: at any time, only one person is
in control.  Implemented in team teaching, it becomes: *you explicitly
know who is in control* (the **director**).  *The director is
responsible for understanding the current situation and checking with other
instructors, but in when you just need to something and no one has
strong opinions, you don't debate, the director decides.*  The main
difference of Model 1 and Model 2 above is "is the director the one
mainly explaining new material, or the one asking questions".  There
are also multiple layers of director: there may be the director for
the whole course, and the director/"conn" for the lesson.

We can't tell you what works best for you.  But the models above and
thinking about who the director is should let you have an efficient
discussion to decide your model.  The need for a director is why we
don't recommend fully equal co-teachers.  Instead, divide the course
into parts and use the two models for each part.

- Of course, there are other roles in a workshop.

  - The **HackMD watcher** pays particular attention to the audience
    questions.  They might be a different person from the co-teachers
    and they can interrupt anytime.
  - The **Meeting host** manages the meeting itself.
  - The Director could be completely separate from the people on
    screen, and somehow sending signals to the teachers as needed.
    But, unlike scripted media, the course reacts more to the audience
    and it is better for the director to be in the lecture.

- If you ever go off-plan, that's OK.  You can discuss during the
  lecture so the audience can know what you are doing and why.  You
  *want* to adjust to the audience more than you would in a solo
  course.  But at the same time, be wary of deviating too much from
  the material that the watchers have, since it will be disorienting.

- Two people works well.  With three, it's hard to allow everyone to
  speak equally and people tend to jump on top of each other in the
  gaps - or no one talks, to give others a chance to say something.
  You could have particular segments where different pairs of
  people adopt the main roles, and others speak up if they want.  Or,
  at that point, make it a panel discussion format (multiple
  presenters and one interviewer)

- Of course, it helps to have a good plan of what you are going to
  do.  But if only one person knows that plan, this strategy can still
  work, especially if that person is the presenter in model 2.

- The less preparation you have, the more useful it is to strictly
  define the roles of each person (to ensure someone is in charge of
  moving it forward).

Please send us more suggestions to add to this list.



Preparation
-----------

This is one proposed model for preparing for team teaching:

- Talk with your co-teacher.  These hints assume a two-person team.
- Decide what material will be covered, overall timing, strategy, etc.
- Divide up the material.  In each section, decide the model to use
  and roles.  If in doubt, starting with the guide/demo-giver division
  with the stronger instructor as guide works well.
- Decide who will be the director for each part.  Perhaps a good idea
  is to keep it consistent: the guide is always the director.
- At least one person prepares the outline (the order of topics to be
  presented, key questions to ask, etc.) - usually the guide or
  interviewer.  The guide or interviewer
  should be comfortable with it (and could even do it mostly alone),
  everyone can give comments and make sure to read it at least once.
- Run as above.
- You don't need to plan every step in detail but it can be useful to prepare
  the session together and step through the choreography (e.g. "now I will show
  this and then give you the screen and then ask you to do this ... you will
  lead this 20 minute block and then I will lead that 20 minute block and
  please ask me questions while I present X").

Then, just go!  Don't worry if it's not perfect, if either person
wonders what to do next, just pause some or ask the other.  This
imperfection is what makes it more dynamic and exciting, and in almost
all cases the audience has been impressed with the co-teaching
strategy, even if it's not perfect.
