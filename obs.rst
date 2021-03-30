Open Broadcaster Software
=========================

Open Broadcaster Software is an amazing open-source audio/video
production tool.  It's probably not professional grade, but is used in
serious events and will make a non-professional feel professional.
The main point is that, instead of being limited to what your meeting
software can do, you can
- Create more advanced mixes of screens/video/etc
- Send the output to more places (local recording, streaming)
- Do this all better, for example, exclude the audience speaking from
  the recording.

It is a GUI application, so is not that hard to use, but there are a
lot of initial concepts.  This page isn't a comprehensive tutorial,
but will introduce the basic concepts and what you can get out of it,
and you can either figure out the rest or read other tutorials.



Basics
------

.. admonition:: Basic A/V concepts
   :class: dropdown

   streaming
      Media which is delivered to the user continuously.  The term
      implies over the Internet.

   livestreaming
      Streaming of source that is live, delivered in near real-time.
      Lately, it is popularized by livestreaming games and other
      activities, which provides us a lot of accessible tools to use.

   recording


   codec
      Coding and decoding.  In this case, the algorithm used to encode
      and decode sound.  There are many, with different properties of
      compression, CPU usage, etc.  The codec is independent of the
      program actually used to encode/decode.

   container format
      File format that contains the audio/video data.  There are
      different formats, and the container format is independent of
      the codec of the material inside (but not all codecs work in all
      containers).  There are containers for both streaming and
      recorded video.

   bitrate
      Amount of data of the bytestream over time.  Usually measured in
      Megabit (not byte, also note the actual unit is
      Megabit/second).  For example,
      Netflix on mainstream "high" quality is about 5 Mbit, and Twitch
      recommends ~6 Mbit at most.

   encoder
      The program that compresses raw video to the codec for
      distribution.

   constant bitrate (CBR)
      Encoding method where the bitrate does not vary over time.
      Twitch and other live streaming sites recommend this, because of
      the way the Internet works (with a live stream, congestion
      control and other protocols keep a constant flow of data.  If
      there is a sudden increase in instantaneous bitrate, it might
      not be able to keep up and buffers empty, causing lag).  Similar
      considerations apply to other playback modes, such as embedded
      devices, thus the idea of encoding "targets" (profiles optimized
      for certain classes of devices).

   variable bitrate
      Encoding method where instantaneous bitrate varies depending on
      how much information is needed at each instantaneous point of
      time, to encode the complexity of the current scene.

   x264
      A common open-source encoder.  Used as a backend for many
      different programs.

   crf
      In x264, a variable bitrate encoding mode (constant rate
      factor).  Values are between 0 and 51, but reasonable values are
      low 20s.  For example, 23 is the default and looks good for all
      practical purposes.

   RTMP
      Real-time messaging protocol.  A common protocol for live
      streaming.  It is proprietary, but was later opened and is now
      one of the main standards.



User interface basics
~~~~~~~~~~~~~~~~~~~~~

OBS is a graphical program.  Once you start it up, you see various
things:

.. figure:: img/obs--controls.png

   Basic OBS control layout

Of primary note is the following concepts.

Preview area
   Shows what will be broadcasted or recorded.

Scenes
   A certain layout that can be broadcasted.  On the lower left is
   your scene collection, and you can add, delete, reorder, and rename
   scenes.  By clicking on a scene, you switch to it and it begins
   broadcasting/recording.

Sources
   An image source which can be composed together in a scene.  Scenes
   can be added, deleted, recorded.  Via the preview area, sources can
   be graphically moved around to your liking.  There is a
   comprehensive set of positional and image effect transforms you can
   make.

Audio sources
   You can take audio input from various sources: mainly, microphones
   or as a monitor of a computer audio device (to, for example, play
   sound).  Audio sources are configured in settings, but can be
   muted/have volume adjusted in the respective area of the screen.

There are buttons to start/stop recording/streaming.  These are
configured in the settings.


Configuration
-------------






Basic configuration
~~~~~~~~~~~~~~~~~~~

Here, we will go over the main parts of configuration.  We won't say
everything, since this is graphical program and you can mostly click
around and find your own customization you would like.

File → Settings → Stream
    Here, you would configure the streaming service, if any.

File → Settings → Output
    Here, you configure streaming/recording output parameters.

    Streaming: 2500 Kbps, other options don't matter so much, defaults
    should be fine.

    Recording: Recording format, mp4 (mkv would be better, but we need
    to check that it can be uploaded to common sites). Encoder=x264,
    Rate control=CRF,  CRF=22, Keyframe interval=auto, CPU
    preset=medium (or slower, for better CPUs)
    (slower=use more CPU to do better
    encoding, either higher quality or lower bitrate.  Veryfast--Slow
    is a good range),
    Profile=main, Tune=None

File → Settings → Video
    Here, you set the base size of the picture you will be using.
    You could do FullHD at 1920x1080, or HD at 1280x720.  For vertical
    recording, we recommend you do 840x1080.  Use your chosen value
    for both Base and Output resolutions.  30 FPS.

    When setting your video size, traditionally people tell you to be
    as large as possible.  However, this guide is focused on teaching
    and learning, and or that a) we want our content to be as
    accessible as possible.  There is no need for as many pixels as
    possible, as we often say "present from your smallest screen", and
    you can do that by artificially restricting yourself.  b) We have
    found a vertical screen works well: a learner can have the
    video/stream taking up half of their screen, and the other half.


Click around through the other menus in settings.


Scene configuration
~~~~~~~~~~~~~~~~~~~

After the above, you can set up scenes basically however you would
like.  However, as a starting point I propose these scenes to get you
started (and I propose we standardize on these names, so we can
uniformly script things):

* **Title**, the logos and titles of the event.
* **Gallery**, a gallery of the people presenting (or the one).  When
  presenting from a Zoom meeting, this is a capture of the gallery
  view in dual-monitor mode.
* **Local** is a local screenshare, that you get by capturing your own
  screen.
* **Remote** is a screenshare by someone remote.  It is made by
  capturing the second window of the dual-monitor mode.
* **Notes** is some HackMD


Common types of sources (scene elements) include:

* Static image (e.g. logo)
* Desktop capture
* Single-window capture.  Note that this is smarter than Zoom is,
  since it can capture even if the window is not on top.
* Text
* Solid colors
* Other scenes.  You can make one scene, then insert it into other
  scenes to avoid duplication of certain scene elements.

The source itself can be moved around graphically, which is good for
setting things up.  When there are more demanding needs, the source
transformation can be edited for more precise control.  There are
source *filters*, which can do video transformations.  Some sources
can be cropped in the source-specific config as well.



Audio configuration
~~~~~~~~~~~~~~~~~~~

Audio configuration is simpler than video configuration, since there
are fewer sources going around.  On the other hand, it is harder to
see what is going on so it is easier to make loops.

The main concept is that your computer may have different input and
output cards on your computer.  For example, I can output sound from
some application on my monitor's speakers, while sound from other
applications on the headphones at the same time.  Find your computer's
way to visualize what is going on under the hood.

There are two types of audio inputs:

* **Microphones**, obviously recording from a microphone.
* **Monitors**, recording what is currently being played on another
  sound card.  This is what is used to capture audio from a remote
  meeting, such as Zoom.

You set the active audio input in the application settings.  The
volumes of these can be independently adjusted - you want typical
volume to be in the yellow zone.  (Audio adjustment is a big thing,
which I don't fully know yet)

Under "advanced audio properties" (menu item, also available from the
gear) you have several more options.

* You can do various filters, such as noise reduction.
* You can group audio sources into various **audio tracks**, and the
  stream/recordings can use different tracks.  For example, a person
  may stream with music but leave that out of the recorded video.  Or,
  you might record a video with two different audio tracks, one just
  the presenter and one with presenter + audience.
* You can monitor the audio, which plays what is being recorded back
  over the headphones and speakers for you to check.  Make sure you
  don't make any loops!

High-quality audio is quite important.  I've spent far too long playing
with it, and my conclusion is that I don't know enough to make it
better than what I have now.  I could use a better microphone, but
then I had to add noise reduction and the quality ended up the same as
a "worse" headset microphone that automatically git rid of most
noise.  Your environment (noise, amount of echo) matters just as much
as your microphone.



Recording and streaming
~~~~~~~~~~~~~~~~~~~~~~~

Once you have done the above, you can record and stream by clicking
the buttons.



Projector and loopback output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beyond recording and streaming, there are several more ways to use the
output that can feed into other applications.

With **projectors** you can display the scene locally in a way it can
be re-used.

* The **fullscreen projector** displays the scene to a monitor.  As
  the name says, this could be used to send it to an external
  projector or capture card via HDMI.  Or even preview locally, or
  capture via a online meeting screenshare.

* The **windowed projector** does similar, but makes a new window that
  can be moved and resized.  This can be captured as a single-window
  screenshare in a video application.


The **loopback output** creates a **virtual camera device**.  This
appears as a camera, just like the camera that captures your picture.
Other applications can use this as the input just like another
webcam.  So, you could make a fancy scene that replaces your picture.
Or, note that in Zoom you can share screen from "second camera" -
which would use this scene.  (Note in Zoom it will interpret it as a
landscape picture, regardless of what aspect ration you actually use.
Thus, this isn't very suitable for vertical screen sharing.)




Example configurations
----------------------

Recording your own demo
~~~~~~~~~~~~~~~~~~~~~~~

Scenes: Title, Gallery, Local

Online teaching event
~~~~~~~~~~~~~~~~~~~~~

Scenes:

* Title
* Gallery - contains galleryCapture
* Local - capture of your screen, when you need to teach.  Has
  galleryCapture in top-right corner
* Remote: capture of Zoom second window (which has been
  adjusted to be same resolution as your base canvas size).  Also has
  galleryCapture in top-right corner.
* Notes: contains HackMD + galleryCapture
* galleryCapture - contains the Zoom gallery capture.  This gets
  inserted into the other scenes above.

Audio:

* Microphone capture
* monitor of card which has the Zoom output

Outputs:

* Recorded locally.  Start and restart recording after every
  transition. (Better to cut more than less, to have logically
  organized shorter segments.  Also, always keep it recording, in case
  you forget to turn it back on!).

* Stream

* Use windowed projector or Zoom capture to send the output directly
  to a Zoom meeting.  But, that requires careful audio routing.
