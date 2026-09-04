Broadcaster
===========

This page explains the setup and how-to guide for the OBS broadcaster.
This person manages the technical setup of :doc:`OBS <obs>` and thus
the streaming.  This person often is, but does not have to be, the
:doc:`director` who switches the scenes and manages the broadcast
after it has started.



Role of the broadcaster
-----------------------

As the broadcaster, you manage the OBS application that captures Zoom
and sends it to the world.  This is different from:

* The **Director** manages the scenes and the overall flow of the
  workshop (switches scenes, cues instructors when to start talking,
  shares HackMD during the breaks).  This person is often the
  broadcaster, but for clarity we use more precise terms.

* The **Host** is the interface between the instructors and the
  audience: e.g. announcing instructors, keeping to the schedule,
  etc.).  They are very often the same as the Director.

* The **Instructors** connect to Zoom and teach.  If there is no
  designated director, at least one instructor needs to know a bit
  about that.

The broadcaster has a lot of preparation work to do the first time
they get set up (future courses aren't so bad).  They should expect
some panicked fixing of stuff right before each course starts.  During
the courses themselves, the broadcaster is mainly sitting back making
sure nothing breaks.



Initial setup
-------------

Prerequisites:

* A somewhat powerful computer dedicated for broadcasting (not used
  for teaching as an instructor, the broadcaster *can* use an
  instructor computer, but that is much more complicated).
* Stable internet connection (speed is not too important these days).

  * 20/5 download/upload Mbps is probably plenty good.  100/10 Mbps is
    far more than is needed.

  * Wired connections, rather than wireless, are better (WiFi,
    non-cellular uplink).  However, you probably know your overall
    stability the best: you want a continuous, smooth connection
    without much `jitter
    <https://en.wikipedia.org/wiki/Jitter#Packet_jitter_in_computer_networks>`__.
    However, OBS settings can be tuned to have a larger buffer to
    handle this (but that introduces latency in the broadcast).


Software installation:

* `Install OBS <https://obsproject.com/>`__ (Linux, Mac, Windows -
  this is a mass market product so there is good support)
* Zoom (but you likely already have that)

Zoom setup:

* Install Zoom.  There's not much you need to do differently.

* Some Zoom settings:

  * General → Use dual monitors → yes.  Despite the name, this gives
    Zoom two *windows*: one for the gallery view, one for the
    screenshare (or active speaker if there is no screenshare).  You
    need two monitors plugged in, though, otherwise the mode doesn't
    work.

  * General → Enter full screen automatically when starting or joining
    a meeting → false

  * Screen Share → Enter full screen when a participant shares screen
    → false (important)

  * Screen Share → Scale to fit shared content to Zoom window → true.

OBS setup:

* Clone the `obs-config repository
  <https://github.com/coderefinery/obs-config/>`__.  This contains some
  pre-made scenes which will set your OBS up for teaching nicely.

* Import the latest TeachingStreaming profile
  (Profile → Import → ``obs-config/profiles/TeachingStreaming-v*``).  This contains things
  like audio and encoder settings

  * TODO: this may need adjustment for your particular situation.  At
    least things like file paths will need to be adjusted.  Look at
    the obs-scenes readme for more information.

  * Most importantly, this sets it to 840 horizontal × 1080 vertical
    (portrait mode).

* Import the Teaching_Streaming_ZoomCapture scene collection (Scene
  Collection → Import →
  ``obs-scenes/scenes/TeachingStreaming-v*``).

* You now need to configure some window captures, for example, you
  need to tell OBS which window has the gallery of all instructors in
  it.  From the "Scenes"

  * In one of the scenes like ``Screenshare``, change the sources
    ``ZoomMeetingCapture`` to the window named ZoomMeeting, and the
    source ``ZoomCapture`` to the window named Zoom.

  * In the scene scene ``Notes``, change the ``HackMDCapture``
    source to the notes window you are capturing

  * (optional) In the scene scene ``BroadcasterScreen``: configure
    your local desktop capture.

* Configure the audio

  * Settings → Audio → Desktop Audio → "Default" (or if you want,
    select an explicit device).  This is what will capture Zoom by
    monitoring your speakers/headphones.

    Note: prevent audio feedback!  Be careful if you set this to
    speakers, and you have a separate computer which you use for
    teaching with a microphone that would hear those speakers: you
    would get feedback.

  * Settings → Audio → Mic/Aux Audio → "Default" (or whatever device
    you want).  This would capture that computer's local microphone,
    if you use it.  (More likely, you would join the meeting as an
    instructor, and thus use a separate computer to speak to people)

  * From the main OBS scene, rename the audio devices:

    * Bottom panel → Audio mixer → one of the devices → gear icon →
      Rename →

      * Desktop capture to "Instructors"
      * Mic to "BroadcasterMic"

* Configure obs-websocket (set the listening socket + authentication).

  * Tools → Websocket server settings → {Enable websockets
    server=true, Server port=4455, Enable authentication=true,
    Password=something}.

* Begin the websocket proxy.  This accepts incoming connections with
  SSL, filters to only allow known safe requests, and then forwards
  the connection to OBS.  The password authentication is proxied to
  OBS, so there isn't a separate password set here.  ``python3
  obs_cr/websocket_proxy.py 127.0.0.1:4456 [other options]``


* Allow outside connections.  On of these two:

  * Use `ngrok <https://ngrok.com>`__ to forward the connection
    (including SSL).  Read more from the obs-websocket documentation:
    https://github.com/obsproject/obs-websocket/blob/4.x-current/SSL-TUNNELLING.md
    .  Note that the free plan limits to 4 simultaneous connections
    and the connection information will change every time you restart,
    which is not great.

  * Configure your router/firewall to allow incoming connections to you
    IP address, on the port configured above.  (it is this external IP
    address that you need to share with other instructors.

* Verify the obs-tablet-remote connection (see TODO director-setup).

* Share your IP address, server port, and
  password with your other instructors.



Before each day checklist
-------------------------

* Set Twitch stream data: stream title, stream description, channel
  about page.

* Configure and check streams

* Test everything

* Basic information private message::

    * zoom info: 
    * zoom link: 
    * attendee hackmd: 
    * notes hackmd: 
    * live preview: 
    * control panel: 


Before each broadcast checklist
-------------------------------

* Ensure anything from the above is done (obs-tablet-remote
  connection, scene layout, etc).

* Ensure Zoom scenes are correctly captured, flip through them to
  verify.

* Wait for first instructors to join.

* Zoom: Disable sound on participants joining

* In zoom, right click on a participant without video and "Hide
  non-video participants".  You may need three participants in order
  to do this: if you have fewer, join through a browser or something.

* Make other instructors co-hosts in the Zoom so that they can share
  screen without the other person stopping.

* (rkdarst, with controller): synchronize button lights with
  zoom/OBS controls

* Start recording / start streaming ~20-30 minutes in advance, with
  audio muted and on the title card scene.  Start recording at the
  same time as streaming so you don't forget it!

* Hand it off to the director (possible yourself) to flip the audio
  and scene once icebreakers start.



During the broadcast
--------------------

* You can not share screen with Zoom (it messes up the windows:
  screenshare becomes gallery, the old gallery window disappears).

  * Instead, there is a separate OBS scene for local screenshare.

  * **But we recommend using a separate computer for broadcasting and
    instructing**, to avoid this problem.

* For the most part, the director does the scene switching (and you
  might be the director)

* You don't need to always be in front of the broadcasting computer,
  but be available in case there are emergencies.



Common problems
---------------

* **Internet connection goes down**

* **OBS crashes** While this happens somewhat often during testing,
  during live productions, when the settings are not being changed, it
  has never been observed.  Set all settings in advance, and maybe
  quit and restart right before starting the broadcast.

* **Audio is capturing the wrong inputs, or audio quality is bad**

  So once when broadcasting, the audio quality was horrible.  It
  turned out that the sound system got confused and the desktop audio
  capture (zoom capture) was actually capturing the microphone.  This
  was *not* reflected in the OBS settings.

  To solve this, go to the OBS settings (you can adjust most, but not
  all, settings while a stream/recording is ongoing).  Flip the audio
  devices to "disabled", then back to what it should be (possibly you
  need to save in between?).

  It's possible there are other times you need to adjust the audio.

* **I have HackMD open in view mode (to share) and HackMD open in edit
  mode (to edit), but OBS keeps switching to share the editable
  one**.  OBS seems to go by window title.  Try this: Use a different
  browser, or run one of them in private mode (so that the title is
  different).



Broadcaster practice
--------------------

1. Start OBS and import the scenes
2. Start Zoom and configure OBS to capture the Zoom windows.
3. Now we try to get the control panel working.

   a. Clone obs-cr
   a. Run obs_cr/websocket_proxy.py with the right arguments

4. Get the local headless client working (this listens to signals and does
   stuff like run the xdotool command to resize windows or scroll notes.)

   a. obs_cr/headless.py

5. Practice switching scenes
6. Practice making scene presets and switching to them
7. Practice scrolling the notes
8. Use your headphones to monitor the sound (audio advanced settings)
9. Include the music/jingle in the recorded video.  Now remove it from
   the recorded video.  (I found it's better to leave it out because
   it affects transcription.)



See also
--------

- There is plenty about OBS and streaming online, since it is a big
  business now.  You can find answers to most questions once you know
  the basic theory.
