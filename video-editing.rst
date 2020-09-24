Video editing
=============

The purpose of this page is to give video processing volunteers a
starting point.  (It also has some hints for workshop organizers).

For some of our online lessons, we release videos on YouTube.  This is
not necessarily for brand new people to watch and learn the material
(though they may), but especially for people who attended the workshop
to review what they saw.  As such, it's more important to get them
published fast, than make them perfect.


What we want
------------

Our workshops consist of lectures, demo, and exercises in breakout
rooms.  We record the main Zoom room, and also livestream the main
room via Twitch.  We would like the video of the workshop to be
processed so that it can be released on YouTube.  This should not be a
major production: it is more useful to those who want to review what
they saw in person, rather than a new person watching.

We will provide the following:

* Raw video files (probably two copies one recorded from Zoom and one
  from Twitch - so there is a backup.)
* List of lessons (= final videos) and which raw files contain them
  and when.
* List of instructors

We want out:

* One processed video file per lesson.
* With irrelevant breaks removed.
* Without any video from learners.  We use Zoom so that learners
  should not appear in the stream, but we can't be sure it works so
  this needs to be checked.

The rough process is:

* Load up the right video files in the editor.
* Find the start of the lesson (hint: look for a change of
  instructor - ask us if you need help!) and cut off the stuff before.
* Watch through the videos.  Most of the lecture parts are fairly
  standard and can be fast-forwarded through (it's rare for a
  learner's picture to appear here).
* Cut out the idle time during breaks.
* In exercise sessions, learners go to breakout rooms, which are not
  recorded.  This part can be cut out, *but* sometimes the instructor
  stays in the main room to do the exercises for the stream.

* Don't be too precise.  We aren't trying to make a masterpiece to end
  all masterpieces, but a something for those who were at the workshop
  to refer back to.  So:

  * Imprecise start/stop/break times are fine
  * Other random off-topic chat is fine
  * Voices of learners is fine and expected
  * **Video** of learners is **not ok** (really, this is the only
    thing that needs care).




Before/during/immediately after the workshop
--------------------------------------------

- From day 1, advertise that "the workshop may be recorded and put on
  YouTube.  We will prevent any pictures and names from going there,
  but your voice may be.  Please don't include your name in hackmd
  unless you accept it may be published.  We support your right to be
  anonymous in this workshop."

- Same announcement at the start of the workshop.

- Record in zoom.  Note: when you start the recording, make sure that
  someone is currently sharing the screen, *and* the screen is a good
  size (e.g. normal Full HD, as opposed to some vertical shape).  The
  dimensions when the sharing first starts determines the dimensions
  for the entire course.

- Immediately after workshop, go to Twitch and download the raw
  streamed version.  You have to be logged in as the channel, then the
  option is naturally provided to you.

- Choose some standard, shared place and immediately upload videos
  there.  Recommended naming scheme::

    day1-topic1-topic2-zoom.mp4
    day1-topic1-topic2-twitch.mp4


Processing
----------

Processing principles:

* **Remove any participant videos, if they accidentally make it into
  the video file**.  This is really the only serious rule in the
  processing, if we didn't have to check this we could just upload the
  raw ones and it would be good enough.
* Create one final video per lesson in the workshop
* Work incrementally, upload processed ones when you can, get quick
  feedback.

If it's not clear, the course organizers will provide a list of the
lessons (final outputs) and the respective inputs (which source files
go into it).


You can generally:

* Use some video editor

  * iMovie on Mac
  * OpenShot is a simple cross-platform editor (`tutorial
    <https://cdn.openshot.org/static/files/user-guide/quick_tutorial.html>`__)
  * (please give more ideas here)

* (so far, this is not a general "how to edit video" guide... you will
  need to find one for your editing program)

* Create a new project for the output (e.g. the Jupyter lesson)

* Import the raw video files which contain Jupyter (e.g. day 4).  If
  one lesson is split over multiple files, combine them.

* Cut off the part before and after the lesson itself (saving
  frequently).  You'll have to figure out the start and end times,
  this may be hard when there are several files.

* Begin watching the lesson.  Look for the following things:

  - Break time?  Exercise session with irrelevant stuff in the video?
    Cut the time out.

  - **Any non-instructors pictures in the stream?**  Cut it out.
    Sometimes you might need to blank the picture while

  - Don't be too perfectionist - the goal is to get something done,
    not maek the perfect videos.

* Export the videos with a high quality, e.g. ``jupyter.mp4``.  It
  will go to YouTube which will render lower resolutions, so you don't
  need to worry about this so much.

* Upload the videos to the ``processed`` subdirectory of the google
  drive.  Do this immediately, video by video.  It's better to get
  continuous feedback on this.  You are done!


Publication
-----------

We upload them to YouTube (not that we agree with all the ethics of
YouTube, but it seems like the least bad and most useful of the
options).

* Preview the processed videos, do a quick check for any issues.

* Upload to the channel.  For one workshop, put all related videos
  into a playlist.  CC-BY license.

* This is a prototype channel description you can copy::

    git-intro 1/2, CodeRefinery 25.may-4.jun 2020 day 1

    Day 1: git-intro: LINK-TO-LESSON

    Part of a series of video recordings of the CodeRefinery workshop,
    25.may-4.june.  CodeRefinery teaches intermediate software
    development skills to researchers in the Nordics.

    Workshop page: LINK-TO-WORKSHOP
    Q&A for day 1: LINK-TO-HACKMD

    (table of contents below)


* Create a **table of contents** (can be done later, after uploading).
  This divides the videos into chapters, with clickable links in the
  description and labels in the video's time slider. In the bottom of
  the description, put this text and it is automatically parsed::

    00:15 Introduction
    02:30 Motivation - https://coderefinery.github.io/git-intro/01-motivation/
    17:17 Basics - https://coderefinery.github.io/git-intro/02-basics/
    38:29 Staging - https://coderefinery.github.io/git-intro/04-staging-area/
    ...

  You may want to ask someone for help with this, since it can take
  some time to go through the videos.

  Example with table of contents: https://youtu.be/r1tF2x5OLNA
