# Teaching via livestreaming

We've all done a lot of teaching via Zoom, but the CodeRefinery
livestream is a new concept.  This introduces teachers/helpers to the
idea (and for a detailed reference, see {doc}`coderefinery-mooc`).

```{admonition} Video

Watch a demo on YouTube: <https://www.youtube.com/watch?v=WjmttAniZX8>.
(When watching, also carefully read the video description/chapter
titles, which provide more the explanation of what is going on).
```


Compared to Zoom teaching:

- You are in a Zoom meeting with only instructors/staff
- Someone (not you) captures this meeting and broadcasts it via
  livestream to all the audience.
- The audience can't directly talk with you (but when there is a large
  audience, who does anyway?).  Instead, always say things like "What
  do you think?  Write in the HackMD. [proceed to screenshare it and
  discuss answers]"
- You don't need to worry much about managing the audience.  Others do
  this and relay information as you need.  You should pay more
  attention to HackMD.



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



## Screensharing

You can share your screen normally via Zoom.  The livestream is fixed
to an aspect ratio of 840 pixels wide × 1080 pixels high (this is so
that the learner has half of their screen available).  **You can not
do a full landscape live-coding follow-along screenshare (nor is this
good practice in other workshops).**

* In **Zoom**, you can either share one window or Advanced → Share a
  portion of the screen → move the overlay to a portrait view.  Don't
  worry about making it exactly 840×1080, OBS automatically fits it
  and we can adjust it during the setup time.

* If you have a landscape presentation (as opposed to live coding),
  just share your whole screen, and the OBS operator will scale things
  properly if it doesn't automatically work.  Note that the 4:3 aspect
  ratio is better than 16:9, but that usually has black bars on the
  side.  This can be removed via OBS.

* Don't stop screenshare unexpectedly - wait for the broadcaster to
  switch to gallery view.  **If you stop screenshare unexpectedly, the
  stream reverts to someone picture full-screen.**  Because of Zoom
  "dual-monitor mode", sharing screen does not prevent the gallery
  from showing.



## HackMD and audience feedback

HackMD (or similar document-based things) is our preferred
communication system.  The biggest problem is that it is *too* useful,
and too many people ask questions, which will easily overload you.  To
solve this, we have co-teachers (non-typer can watch HackMD), HackMD
helpers (watch and answer basic questions).

There are several general strategies:
* Occasionally screenshare the HackMD.  This emphasizes to the
  audience that questions there *do* get noticed.
* Rely on other helpers to answer most questions.
* During Q&A time, go to the HackMD and comment on the most important
  questions.
* Call on co-teachers, "do we have any good questions from HackMD?"
* Co-teachers should be more than willing to interrupt with relevant
  questions right away.

You can't use Zoom polls and so on.  Instead, use HackMD cleverly.
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
