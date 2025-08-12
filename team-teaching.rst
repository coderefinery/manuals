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
fill all silences, instead of yielding to make a conversation.

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

The general idea is that you want to make your teaching event a
conversation.  Pay attention to news broadcasts, game streams,
podcasts, etc. to see this in action: it makes things much more
interesting to listen to.  Usually, they try to do this by having two
different roles that complement each other.

The basic idea is that you want to keep a constant *conversation*
going.  This can be a mutual discussion, one person explaining big
concepts and one the details, one person asking
questions and the other answering, or some other combination.  *This
is not simply two people taking turns in different sections.*

With team teaching, there is less need for the instructors to prepare
every single thing perfectly, since you can rely on two brains to get
you through areas you haven't perfectly prepared.  In fact, this is
good, because then your learners will see things go slightly wrong and
your live debugging (it will look like you wanted something to go wrong to teach it).

Still, you want to agree on a plan in advance, and know what the roles
will be.

.. pull-quote::

   One of the most important principles of ship handling is that there
   be no ambiguity as to who is controlling the movements of the
   ship. One person gives orders to the ship's engine, rudder, lines,
   and ground tackle. This person is said to have the "conn."

   — James Alden Barber, 2005, "Introduction", The Naval
   Shiphandler's Guide, p. 8. Mark B. Templeton, via `wikipedia <https://en.wikipedia.org/wiki/Conn_(nautical)>`__

As the quote says, in any large enough operation, multiple people are
involved, but responsibilities should be clear.  At least, one person
should have the responsibility for time-keeping and overall flow.  This
should be integrated into your co-teaching plan.

We propose some basic models, but of course there is a continuum.  And
you can (+should) switch up models, or roles within the model, in
different sections.

.. admonition:: Example of a teaching plan

   R and S usually teach a HPC tutorial each year via co-teaching.  The
   general plan is:

   * Day 1: "talker and typer" format.  R is the talker (primary) and
     S is the typer (secondary).  R goes through the main points and
     tells S what to do in the demos.  S pretends to be learning and
     doesn't do anything until told.
   * Day 2: swap roles but otherwise like day 1
   * Day 1 and 2, sections without exercises (for example, "what is
     slurm?"): "interviewer and expert" format.  Switch primary to
     "interviewer" and secondary to "expert", and the primary
     "interviews" the expert to explain what's going on.

   This is implemented in the following teaching plan (see
   :doc:`teaching-plan`).
		
   https://hackmd.io/@AaltoSciComp/2025kickstart-tritondemos



Model 1: Guide and demo-giver (talker and typer)
------------------------------------------------

One person serves the role of **guide (talker)**, explaining the big picture
and possibly even the examples.  The **demo-giver (typer)** shows the typing
and does the examples, and could take the role of a learner who is
asking about what is going on, the person who actually explains the
details, or an occasional commenter.  Anyway, the guide is the one
navigating through the course and bringing up material in a logical
order for the audience and "has the conn".

Hands-on demos and exercises work especially well like this.  Here,
the guide would follow the outline and serve as the director (see
below).

.. admonition:: Example of "guide and demo-giver"

   In our HPC course, we use this for the main tutorials.  One of us
   explains the material and says what to type, the other one types
   the demos.  The instructors swap roles depending on interest.


.. csv-table::
   :delim: |
   :header-rows: 1

   Guide                      | Demo-giver
   Introduces most material   |
   Goes through theory        | Asks questions that a learner may ask
   Introduces type-along      |
   Explains steps of type-along | Types during type-along
   Asks questions to Demo-giver during type-along | Explains details what they are typing and what happens
   Looks at Notes during type-along  |  Looks at Notes during theory
   Discusses during Q&A       | Discusses during Q&A



Model 2: Interviewer and expert
-------------------------------

In this case, there is an **interviewer** who pretends to be a learner
is asking questions to an **expert** who is mostly explaining.  The
**interviewer** serves as a learner or spotter, fills in gaps by
asking relevant questions, and tries to keep things on track.  The
interviewer "has the conn".

Either person could type and do the demos.

.. admonition:: Example of "interviewer and expert"

   In our HPC course, we would use this for our intro to Slurm.  There
   are no demos at that point, so one person prompts the other with
   questions about Slurm.


.. csv-table::
   :delim: |
   :header-rows: 1

   Interviewer                       | Expert
   Asks questions to expert          | 
   Follows up with learner questions | Answers questions using their special knowledge
   Pushes forward though the material |
   Asks questions that a learner may ask |
   Introduces type-along             |
   Explains type-along and material  | Explains type-along and material
   Looks at Notes most of the time   | Looks at Notes when possible
   Discusses during Q&A              | Discusses during Q&A



Model 3: Teacher and student
----------------------------

In this model, someone takes the role of the **teacher** and gives the
lesson.  The **student** pretends to be the student and asks relevant
questions.

This is closer to normal teaching, so feels more natural to do.  The
big disadvantage is that it's the tendency of the presenter to keep
talking, and the tendency of the interviewer to be nice and not
interrupt.  This negates most of the benefit you would hope to have,
but is much better than solo teaching.  The "Guide and demo-giver" is
usually better when there are demos and "Interviewer and expert" when
there aren't.  The teacher "has the conn".

.. admonition:: Example of "teacher and student"

   In our HPC course, this isn't used so much.  I might use it if I
   was co-teaching something like GPUs or MPI, which I don't know that
   well.  I'm not confident in what to type, so I really am much more
   like a student than a demo-giver and I don't expect to contribute
   much to the content.  Of course it's close to "guide and
   demo-giver" anyway.


.. csv-table::
   :delim: |
   :header-rows: 1

   Teacher                           | Student
   Guides through the material
   Gives demos                       | Asks questions a learner may ask
                                     | Watches the Notes closely
   Keeps time                        | Reminds about time



Hints
-----

With more than one person, there is a risk of seeming uncoordinated
when the team doesn't know who is supposed to move the lesson forward.
It's not bad to have short discussions to decide what to do next, it
makes the show seem interactive and like it is responding to learner
needs.  But if it happens too much, it becomes noticeable.

As quoted above, you could adopt a principle which exists in many
domains: at any time, only one person is in control (we call them the
"primary").  *This person is responsible for understanding the
current situation and checking with other instructors, but in when you
just need to something and no one has strong opinions, you don't
debate, the primary decides.*

Note there can be "primary" for the whole lesson preparation, that is
different than the "primary" for some sections.

We can't tell you what works best for you.  But models 1 and 2 above
tend to work very well and give a clear "primary".  The need for
someone to "have the conn" is why we don't recommend fully equal
co-teachers.  Instead, divide the course into parts and use the two
models for each part.

- Of course, there are other roles in a workshop.

  - The **Notes manager** pays particular attention to the audience
    questions.  They might be a different person from the co-teachers
    and they can interrupt anytime.
  - The **director** manages the flow of the course itself.
  - The Director could be completely separate from the people on
    screen, and somehow sending signals to the teachers as needed.

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
  experts and one interviewer)

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
  Review the schedule from last time and make a schedule for this
  time, with timings, breaks, etc.  Usually you don't need to get
  creative - use what works.

- Divide up the material.  For each episode, decide the model to use
  and roles.  If in doubt, start with the guide/demo-giver model
  with the more experienced instructor as the guide.

- For each episode, one person prepares the outline (the order of
  topics to be presented, key questions to ask, etc.) - usually the
  guide or interviewer.

  - You don't need to plan every step in detail but it can be useful
    to prepare the session together and step through the choreography
    (e.g. "now I will show this and then give you the screen and then
    ask you to do this ... you will lead this 20 minute block and then
    I will lead that 20 minute block and please ask me questions while
    I present X").

- Discuss the plan together and make any revisions as needed.

- Do one run-through.

- Teach as planned.

Then, just go!  Don't worry if it's not perfect, if either person
wonders what to do next, just pause some or ask the other.  This
imperfection is what makes it more dynamic and exciting, and in almost
all cases the audience has been impressed with the co-teaching
strategy, even if it's not perfect.
