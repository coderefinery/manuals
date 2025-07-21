# Instructor introduction

This page gives general instructor information: the starting point on
your journey.


## What's it like as an instructor?

We teach online, livestream, and with *co-teaching*. That means the
lesson is a conversation between two instructors, instead of one
person alone and many students.  It's especially easy to get started
this way: co teach with someone experienced!

You can see a demo of what livestream co-teaching is like here:
<https://youtu.be/WjmttAniZX8?t=3> (15 min, many different scenes).



## Starting materials

Read the material in the left sidebar.

Reading elsewhere:
* [CodeRefinery instructor
  training](https://coderefinery.github.io/train-the-trainer/)
* [Carpentries instructor training](https://carpentries.github.io/instructor-training/)



## The instructor experience

Most of our workshops are very collaborative arrangements: you are
rarely alone.  This is one way of looking at it:

* Divide up the lessons.  There is a primary (overall makes sure it
  happens) and secondary (equally active, but not with "ultimate
  responsibility") assigned to each lesson.  We try to have at least
  one person experienced with the lesson.

* Have a chat with someone else (probably another instructor or
  expert helper) before teaching.  We encourage this for
  everyone, even experienced instructors, to better transfer knowledge
  among each other and stay up to date with the latest developments.

* Install the CodeRefinery software environment (so you can test the
  same way as learners).

* Go over the lesson: read everything, and do all the examples.
  Hopefully, this is relatively fast (remember, learners at at least
  5x slower than you, so you can't teach that much).

* Most importantly, update any examples that don't work with the
  CodeRefinery environment.  Common problems include: Github or
  software changing something.

* Make anyy other changes that are needed.  See the hints in the
  lesson development section, but in general want minimal changes:
  most things exist for a reason.  It's a big try to try add in more
  stuff that is missing: there is hardly time for everything in there
  already, stuff is usually left out for a reason.

* It usually helps to do one full run-through with your co-instructor.
  (In fact, if you do one run-through, that's usually all you need!)

* Do a livestream practice session, if this is new to you.

* Teach together!  It won't be perfect, but that will help to keep the
  attention and make it seem like a "thing".  Adapt as needed - we are
  around.

### Main vs breakout sessions

As an instructor, when preparing your lesson you first need to decide
how to balance between the main room and breakout sessions.

- **Clearly say when a learner watches, when they type along, when
  they should work on something independently as an exercise.**
- CodeRefinery is traditionally a hands-on workshop, so exercise
  sessions should be a large part of the workshop.  Usually, it's good
  to try to minimize talking and let people get to the exercise
  sessions as soon as possible.  The written material should support
  this.
- We usually keep the main room mostly for general discussions. Small
  exercises or polls can also be done in the main room, for all
  hands-on exercises we divide the learners into breakout-rooms each
  with one team leader.
- To give you an idea about how the work in the exercise sessions is
  going, monitor the Notes closely and if time allows try to visit a
  few breakout rooms to see how it is going and if needed adjust the
  timing.


### Preparing for the breakouts (in the main room)

**As an instructor, you need to clearly define what the tasks of each
exercise session is (even if it is just "explore and discuss").**
Online courses need more **"meta talk"** about how you expect things
to go, since it's not as easy to read the room or fill in expectations
later (distractions, hard to communicate to breakout rooms after
opened).

- Clearly say what the tasks of the breakout session will be.
- Put that task and a link to the part of the lesson in the hackmd.
- Clearly say how long each breakout session will be (make sure it's
  long enough and adjust during the exercise session if needed)
- Clearly say if things in the future will depend on this exercise (is
  someone completely lost if they don't make it to the end.  Halfway?)
- Try to make breakout sessions longer:
  - imagine a 5 minute overhead for each session, getting people
    there, deciding who does what, acquainted with what they need to
    do, and debugging problems.
  - 10 minutes is quite short (5 min figuring out what to do + 5 min
    doing), so 20 minutes is best.
  - **Can you say less and let people discover it for themselves?**

As a team leader, if anything is unclear to you, it is very unclear to
others. Comment/Ask in the HackMD or speak up and ask! 



## Top issues new instructors face

```{figure} img/screenshare/s10-kickstart-prompt-log.png
:align: right
:width: 50%

An example of a beautiful screenshare.  Note the portrait orientation
(you have half the screen free for notes and HackMD, learners have
half the screen free to do their own work).  The terminal is
dark-on-light, a minimal prompt, no other fancy shell distractions,
there is a shell history visible, and slightly distinct colors between
the web browser and the terminal.
```

- Breaks are not negotiable, minimum 10 minutes.

- Breakout sessions too short.  Make them as long as possible, don't
  expect to come back for new intro, then go back.

- People will accomplish less than you expect.  Expect learners to be 5
  times slower than you, at best!

- All the other tools and stuff will go wrong.  Try to not bring in a
  dependency when you don't need it.

- Trying to accomplish too much: it's OK to cut out and adapt to the
  audience.  Have a reserve session at the end you prepare, but are
  ready to skip.

- Not clearly separating (in the learner's mind, by meta-talk), the
  differences between *demo*, *type-along*, and
  *exercise*/*exercise-prep*.
  - Demo and type-along are hard to do at the same time: they are very
    different types of focus
  - Type-along and exercise of the same thing are not good to combine,
    leads to duplication

- Explaining how, but not why.

- Running out of time to making your environment match the
  learner's.

- Running out of time to set up good screen sharing practices
  (terminal history, portion of screen, remote history) in advance.

- Assuming learners remember what they have already learned, or know
  the prerequisites.  Or have stuff installed and configured.

- Not managing expectations: learners think that you will accomplish
  everything, and feel sad when you don't.  Instead, say explicitly
  what everyone should follow along, what you might want to watch,
  what is only a demo.

- Following the lesson as written at all costs.

For {doc}`livestream courses <instructor-stream>`:

- Worrying too much (forgetting that there is a co-teacher and break
  time where you can discuss and plan your next step).

- Speaking like learners should be able to speak up with voice,
  instead of "answer in HackMD or discuss within your groups."

- Forgetting to save time for Q&A: there is *more* Q&A because of
  HackMD.  You might take a few minutes to screenshare HackMD and
  after each exercise session, after each break, after each episode,
  and at the end of each day.

- "Stop screenshare" instead of letting the other person start and
  take it from you.  Or, the broadcaster switching the scene.  Never
  do "stop screenshare".

- Forgetting to screenshare the HackMD during Q&A time (this is the
  most important way learners know it is active, and thus feel a
  connection to the course).

- Forgetting there are multiple ways to attend: not everyone is in a
  breakout room, not everyone has helpers nearby.  Instead, use
  phrasing such as "for those of you in breakout rooms, go there now.
  Everyone, remember to ask any questions in the HackMD, even if you
  are alone."

- Planning to do a demo during team breakout sessions (teams will
  still hear your voice, if they mute the stream it's hard to bring
  them back).

- Sharing a fullscreen, not the 840x1080 portrait layout.

- Showing non-creative-commons material on the stream.
