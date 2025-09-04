# Teaching via livestream

In "traditional" online teaching, there is a "meeting" format: there
is a many-to-many conversation possibility.  But we all know that in a
big enough meeting, most people are silent.  Small meetings work fine,
big meetings are boring.

But large amounts of people can be talked to with the right means: for
example TV and radio reach many people.

We use this idea in livestream courses.  We switch our mindset to
few-to-many communication for primary teaching, and other bettor tools
for many-to-many communication.

```{admonition} Livestream teaching demo video

Watch a demo on YouTube: <https://www.youtube.com/watch?v=WjmttAniZX8>.
(When watching, also carefully read the video description/chapter
titles, which provide more the explanation of what is going on).
```



## The concept

Instructors teach in a Zoom meeting, but there are no students.
Instead, there is a broadcaster/director which runs software which
captures the Zoom windows and livestreams it.  Your teaching is
generally a lot like normal, but you need to be aware that people are
watching you from many different places.

What about interaction?  Well, the meeting would be relatively silent
anyway, perhaps except for a few loud people.  We take the time to go
all in on {doc}`team teaching <team-teaching>`, where two people teach
together as a conversation.  Look around, you you see things often
happen in groups of two: look at two-person news shows or podcasts.

But how do we communicate with the learners?  We use many-to-many
tools, mainly the {doc}`Notes document system <hackmd-mechanics>`,
where many people can write and answer questions at the same time.
People can get instant answers, asynchronously, and anonymously.

Once there is a stream, there are different ways to watch.  We have
had all of:

- Solo learners watching alone
- Groups of people watching in a physical meeting/class room (with
  local helpers for exercises) (sometimes organized by CodeRefinery
  partners, sometimes not)
- Groups of people watching online, but in a Zoom session for doing
  exercises together.
- We centrally organize a Zoom session for exercises, providing
  CodeRefinery helpers and organized breakout rooms with teams that
  CodeRefinery organized.



## Basic meeting setup

There is an "instructor Zoom meeting".  There are no students here,
and everything can and will be captured, recorded, published, and
livestreamed.

* In the call are instructors, the Zoom host, and possibly some other
  helpers who might occasionally comment.
* The cameras of instructors are captured via Zoom gallery view.
  This is show as both a "teacher view" as well as "overlay on
  screenshare".
* If you have your camera off, you will *not* appear in the stream.
  So turn your camera off when you are in the instructor meeting but
  not presenting.  Ask others, but in principle it is fine to join,
  stay hidden, and interact when relevant.
* During the breaks/exercise times, the livestream itself (via OBS)
  gets *muted* and *switched to another scene*.  So, you are free to
  unmute, talk, and chat with other instructors.  This is a great way
  to relax and prepare for the next segments!  This actually lowers
  the pressure to pre-plan every part in advance.
* By the same token, you can join the meeting during the previous
  break to get all set up.
* Zulipchat serves as the overall connection between the different
  parts of the course and instructor backchannel.  This is the least
  important place for the current active instructor to watch (but
  might be useful for a co-instructor or expert helper to occasionally
  check).




## Why livestream?

A livestream workshop allows us to reach an unlimited number of
people, at the cost of not being as interactive as in classroom/zoom
room.  However, we have had great experiences with the following
strategy:

* Learners can't appear on the stream or in any recorded material:
  this is much better for privacy, which is needed to reach a larger
  scale.  It allows us to relase videos.
* There are more diverse ways to attend for different learning styles.
* We can have a critical mass of attendees at every workshop, since
  each workshop is across many institutions.  We couldn't manage many
  small workshops like we used to do.
* Notes as collaborative note-taking tool allows learners to ask
  questions anonymously and everyone can answer these questions
  asynchronously.
* Learners can register to join Zoom breakout rooms, which are
  interactive and team leaders can help with any questions during
  exercise sessions and breaks.
* Learners can also form private breakout rooms or meet in person and
  watch the stream and do exercises together.

While the full livestream setup is a bit complicated, you as an
instructor do not have to worry about anything but your teaching.  We
have setup the whole system in a way that only active instructors are
shown in stream, which makes video postproduction faster.



## What you need to know

* Prepare in advance (all the pages in this section)
* Come to the instructor setup session to test and all.
* When your teaching time approaches, join the instructors Zoom.
  * Stay muted and turn your video off until it is your turn to teach 
  * When it is your turn to (co-)teach,
    * All co-instructors, turn on your video
    * Unmute yourself only when talking
    * Share only the important portion of your screen in vertical mode
    * If you need a reaction from learners, use the Notes
    * Co-Instructor watches the Notes and relays important information/questions
    * Exercises: clearly state which exercises should be done and at what time the teaching continues
  * During exercise sessions and breaks
    * The director will switch to the notes
	* You can unmute, turn on video, and discuss with others about
      what comes next.


## Notes and audience feedback

The Notes document is our preferred communication system.  The biggest
problem is that it is *too* useful, and too many people ask questions,
which will easily overload you.  To solve this, we have co-teachers
(non-typer can watch the notes), notes helpers (watch and answer basic
questions).

There are several general strategies:
* Occasionally screenshare the Notes.  This emphasizes to the
  audience that questions there *do* get noticed.
* Rely on other helpers to answer most questions.
* During Q&A time, go to (and screenshare) the Notes and comment on
  the most important questions.
* Call on co-teachers, "do we have any good questions from Notes we
  should look at?"
* Co-teachers should be more than willing to interrupt with relevant
  questions right away.

You can't use Zoom polls and so on.  Instead, use the notes cleverly.
For example, below you see a poll (people add `o` to make a bar
graph), and a free response:

```
Have you used HackMD before?
yes: oooooooo
no:  oooo

What do you like about it?
- answer
- answer
- .
- .
- .
```


## Control panel

The control panel allows non-verbal communication between instructors.
It has indicator lights which can be pushed and light up for all
instructors, and a timer.  It is also how the director and broadcaster
control the stream, but you don't need to worry about that.

The broadcaster will send the link to you in advance.

:::{figure} img/instructor-livestream--controlpanel.png

The instructor version of the control panel, running on a phone.
Click the "Fullscreen & wakelock" to make it full screen and not
powersave.
:::



## See also

* Every other page in this section of the CodeRefinery manuals
* {doc}`coderefinery-mooc` - broad strategy
* {doc}`obs` - Open Broadcaster Software theory.  Not needed for
  instructors.
