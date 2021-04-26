CodeRefinery MOOC strategy
==========================

This page documents the CodeRefinery MOOC strategy.  It is not a real
MOOC (it's not massive enough yet), but it does reach out from one to
many, and can scale to basically all the world.


Technical setup summary
-----------------------

We have a public broadcast, with goes out via a livestream.
Disconnected from this, people are watching the broadcast in a
*separate* Zoom meeting and doing exercises/breakouts there.  Or,
people can watch via the livestream alone.  Or there can be different
meetings.  Or people could watch recorded videos later.

The mental model here is "Watching TV together".  We collective watch
a show together.  There are periodic intermissions where each watching
community discusses among themselves and works on the exercises.
Everyone feels they are a part of something big and that keeps people interested.

We have clear communication channels from learner→instructor
(HackMD), helpers→instructors (chat), instructors→learners
(livestream).  Of course instructors can directly to the audience
during their breaks.

The **Director** controls the stream and is responsible for keeping
things running smoothly.



Instructors
-----------

There is an **instructor Zoom meeting**.  This is broadcasted via
Twitch, using :doc:`OBS <obs>` (there is usually a separate director
or production manager for this, instructors don't need to worry
themselves with this).

Compared to the classic style, advantages include:

* You are freed from student management, others help manage the
  audience and convey these important parts to you.
* Audio/video is muted during breaks, there is more opportunity to
  discuss and plan what comes next with the instructors.

Disadvantages:

* You lose the direct access to all students (but how often would
  someone speak up anyway?).


Instructors should keep in mind:


* At all times you will have a director to help keep you on track:
  just teach and watch chat (and HackMD when you have time, but others
  do this and let you know).
* You will have a private Zoom meeting with only instructors (and any
  other key helpers who want to be there).
* Share a vertical screen (840 × 1080 maximum).  This allows students
  to keep half of their screen open for their own work.
* HackMD is the main way of receiving questions from students (just
  like in our current courses).
* During breaks and pauses, the livestream will be muted, so that
  instructors (and helpers there) can talk without the audience
  hearing.  This greatly increases professionalism and makes it easier
  to coordinate.
* There is the standard text chat (Zulip) to use to communicate with
  other helpers.
* Of course, you can go join the student room during breaks, other
  sessions, and so on.

* Zoom polls won't work.  We can use another service for that instead
  (e.g. presemo.aalto.fi).

* You will have more than just the registered students in another room
  as an audience.  Your audience includes students in the breakout
  room meeting, livestream watchers, people in their own meetings with
  a private team we don't know about, people broadcasting it to
  physical rooms, people watching recordings later, and who knows who
  else.

  * Try to speak with awareness of this diverse audience.  You don't
    need to change much, but go slowly and give plenty of time, and
    you can say things like "If you are registered, ... .  If you are
    on your own, ... ."

  * Speak in terms of breaks and exercises sessions.
  * Speak in terms of relative times.  e.g. Exercise session ends at
    50 minutes past the hour, at xx:50".
  * Realize there are different learning styles.  Some people will
    attempt all exercises.  Some will passive watch and want demos.

* We propose this general model for each lecture-exercise cycle:

  * Give the lecture part
  * Introduce the exercises
  * Short break (~5 minutes).  People attempting exercises themselves
    go into their other meetings and work on it.  The learners
    attempting it themselves will mute the stream.
  * On-stream, do the exercise as a type-along or demo.  This is useful
    for some audience, and also is very useful in recordings.
  * At the designated time, the learners come back to the livestream.
    Depending on what you want, you could use the outcome of the demo
    to discuss what we learned, do a whole new demo (perhaps faster
    this time), or you go on.

* You should also make it clear to the audience (mainly
  helpers/exercise leaders) what the expectation for each exercise
  session is.  This should be written in the HackMD!

* It is OK to decide you can't make things perfect for every audience.
  The rest will understand this if you make this explicit.


Helpers and supporters
----------------------

As a helper, your job stays pretty much the same.  There is more
emphasis on making sure that all questions and comments are in the
HackMD.

Some helpers can join the instructor meeting and directly relay
questions and thoughts, and in general provide the "voice of the
audience".



Audience and exercise leaders
-----------------------------

There are different ways for an audience to interact.  They can all
happen at the same time.

Main meeting with breakouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, there is a meeting (e.g. Zoom) which has a lot of learners in
it.  There are two options for lectures:

* Meeting host shares the livestream (video + audio)
* Participants individually open the livestream and watch, and go back
  to the meeting when it is time to do exercises.

All audience members ask questions and discuss in HackMD (just like in
regular workshops).  The meeting chat is mainly used for
practicalities, and is not designed to be monitored by the audience.

The most significant risk here is that learners have to mute the
livestream (or turn it off) during the exercise sessions if there are
demos going on while they are doing exercises.  This means we may have
trouble getting their attention.

Stream
~~~~~~

Here, each audience member watches Twitch independently.  During the
exercise sessions, they can work alone, watch the demos, or work with
their own self-organized teams.

Live
~~~~

The stream is broadcast in the physical classroom or meeting room
where a class or team is located.


Open issues
-----------

* It can require some cognitive effort to understand and keep track of
  all of these different channels.  But when we did it in
  January/February, learners picked up quickly and there were few
  complaints in the end.

* HackMD spam: Lately, we have had one HackMD for all students
  (registered or watching via the stream).  There has yet to be any
  spam or trolling problems, but it will happen if we get big enough.
  We need a transition plan to private HackMD if needed.  (Proposal:
  have a backup HackMD. If spam starts, we email the new one and go
  from there.

* Chat/Q&A scaling: Will HackMD actually scale enough for us?  What
  alternatives do we have?
