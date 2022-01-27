Broadcaster
===========

This page explains the setup and how-to guide for the OBS broadcaster.
This person manages the technical setup of :doc:`OBS <obs>` and thus
the streaming.  This person often is, but does not have to be, the OBS
director [todo: link] who switches the scenes and manages the
broadcast after it has started.



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
    handle this.


Software installation:

* `Install OBS <https://obsproject.com/>`__ (Linux, Mac, Windows -
  this is a mass market product so there is good support)
* Install `obs-websocket
  <https://github.com/obsproject/obs-websocket/>`__.  This is also
  fairly widespread, but slightly less so than OBS.
* Zoom (but you likely already have that)

Zoom setup:

* Install Zoom.  There's not much you need to do differently.

* Some Zoom settings:

  * General → Use dual monitors → yes.  Despite the name, this gives
    Zoom two *windows*: one for the gallery view, one for the
    screenshare (or active speaker if there is no screenshare).

  * General → Enter full screen automatically when starting or joining
    a meeting → false

  * Screen Share → Enter full screen when a participant shares screen
    → false (important)

  * Screen Share → Scale to fit shared content to Zoom window → true.

OBS setup:

* Clone the `obs-scenes repository
  <https://github.com/coderefinery/obs-scenes>`__.  This contains some
  pre-made scenes which will set your OBS up for teaching nicely.

* Import the TeachingStreaming profile
  (Profile → Import → ``obs-scenes/profiles/Teaching_Streaming``).  This contains things
  like audio and encoder settings

  * TODO: this may need adjustment for your particular situation.  At
    least things like file paths will need to be adjusted.  Look at
    the obs-scenes readme for more information.

  * Most importantly, this sets it to 840 horizontal × 1080 vertical
    (portrait mode).

* Import the Teaching_Streaming_ZoomCapture scene collection (Scene
  Collection → Import →
  ``obs-scenes/scenes/Teaching_Streaming_ZoomCapture``).

* You now need to configure some window captures, for example, you
  need to tell OBS which window has the gallery of all instructors in
  it.  From the "Scenes"

  * Scene ``_Camera`` → source ``_ZoomGalleryCapture`` right click →
    Properties → Window → select the Zoom gallery view (for me it is
    titled "Zoom meeting").  TODO: adjust the size of this window
    until XXXXX [it looks nice and large]

  * Scene ``_Screenshare-Zoom-Capture`` → source ``Desktop (remote)``
    right click → Properties → Window → select the Zoom
    screenshare/active speaker window (for me it is titled only
    "Zoom").  Adjust the size of this window until it nicely fills the
    preview pane (the ideal size is 840×1080).

  * (optional) Scene ``_Hackmd-Capture``: similar, select the shared
    HackMD

  * (optional) Scene ``_Broadcaster-Screen``: configure your local
    desktop capture.

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

  * From the main OBS scene, rename the audio devices (TODO: this may
    be done in the profile settings):

    * Audio mixer → one of the devices → gear icon → Rename →

      * Desktop capture to "Instructors"
      * Mic to "Local microphone"

* Configure obs-websocket (set the listening socket + authentication).

  * Tools → Websocket server settings → {Enable websockets
    server=true, Server port=(something), Enable authentication=true,
    Password=something}.  Share your IP address, server port, and
    password with your other instructors.

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



Before each broadcast
---------------------

* Ensure anything from the above is done (obs-tablet-remote
  connection, scene layout, etc).

* Ensure Zoom scenes are correctly captured, flip through them

* Wait for first instructors to join

* Start recording / start streaming ~20-30 minutes in advance, with
  audio muted and on the title card scene.

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



See also
--------

- There is plenty about OBS and streaming online, since it is a big
  business now.  You can find answers to most questions once you know
  the basic theory.
