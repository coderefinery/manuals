# Online training manual OLD

```{note}

This hasn't been updated since we developed our {doc}`MOOC strategy <coderefinery-mooc>`.
```

Also please read our [lessons learned](https://coderefinery.org/blog/2020/04/14/first-online-workshop/).

This manual covers general guidelines for conducting online
training as well as specific tips on using [Zoom](https://zoom.us/).


## For the instructors

If you have an old spare laptop, connect to the call as a second "you" and you can
watch and verify your screensharing and fontsize to avoid "Am I sharing the screen?
Hopefully you see what I see."


## How to avoid "Zoom bombing"

- Either set a password or use waiting rooms
- Share connection details only with participants and helpers, not on the web
- Disable file transfer
- Disable "Allow removed participants to rejoin"


## Preparation

- Schedule the meeting/webinar in the online Zoom system
- do not auto-mute participants' microphones, as this also happens when you enter breakout rooms.
- Decide roles:
  - Decide the Zoom host and co-hosts
  - Use panelists? (Zoom webinar feature)
  - Decide instructor and backup-instructor in case of network issues
  - Decide helpers. One helper should be responsible for monitoring
    Zoom, i.e. the chat window, hand-raising and other feedback
- Co-hosts, breakout rooms and feedback controls need to be enabled (on
  website) before the meeting starts. If options are reconfigured, the meeting
  may need to be ended and restarted for them to take effect.
- Create enough breakout rooms at the beginning since this cannot be easily changed during the meeting.
- TODO: set up pre-lesson polling? (zoom feature) Maybe unnecessary in view of pre-workshop survey
- Instructors and helpers should use a reliable camera and microphone.
  Computer microphone might not be enough since audio quality will depend on
  instructor's head angle and proximity to screen.
- Workshop owner creates a HackMD which will be used for collaborative note taking.


## At the beginning of the session

- Allow time at the beginning of the session to debug video/audio and to
  arrange windows. This takes few minutes so better do not start with teaching
  from minute 1.  Plan for an early 5-minute break to debug this.
- We cannot assume that all Zoom participants have the same and up to date
  client and some clients do not contain "sticky notes" feedback or a button to
  raise hands so agree with participants on signals (e.g. typing `\hand` in the
  chat window seems to be standard).-
- We demonstrate how HackMD works and use it in an ice-breaker (roll call or asking a questions).


## Recording of sessions

If you plan on recording and publishing the session, prepare in advance so that
you don't have a difficult editing job later.
Make sure that you (or users) don't show any personal or confidential information.
Think about what happens if users speak: do you ask for permission to publish
in advance (maybe encouraging people not to), or edit it out later (taking
your time later).

If you plan to record the session, make sure that everybody is aware that the
sessions is recorded, informed about how the recording will be used, and gives
consent to be recorded:
<https://support.zoom.us/hc/en-us/articles/360026909191-Consent-to-be-Recorded>

In Zoom it's important to start recording in the form you want the video to be
in (e.g. start recording when screen is shared so that it stays there):
<https://support.zoom.us/hc/en-us/articles/360025561091-Recording-layouts>

Set screen background to black. We saw a glitch in Zoom which caused the
background image to flash above the screen, if it was pure black it would be
less distracting.


## Zoom-specific installations instructions sent out before workshop/lesson

- Recommend to install Zoom app. Browser is possible but more limited
- Test-launch zoom and test microphone, speaker and camera (lower left corner buttons)
- Instruct participants to watch a zoom introduction (TODO: insert link),
  and play around with zoom.us/test to get acquainted with interface.
- Optional: set up virtual background
- "During the workshop, you might be asked by a helper to share your screen.
  Make sure to keep private information away from the screen you share."


### Contingency plans

- Be prepared for intermittent network problems.
- There should be a backup instructor in case the main
  instructors disconnects
- Learners might occasionally experience lag and temporary
  network hickups. This makes it particularly important to
  speak slowly and repeat important topics.


## Breakout rooms

- Breakout rooms can be used both by helpers to assist individual
  learners during an exercise, or for multiple learners working on
  a group exercise.
- When creating groups, the host or co-hosts can choose automatic setup,
  where only the number of groups is selected and the distribution into
  groups is automatic, or manual setup where the host/co-hosts distribute
  learners into groups.
- Host needs to move helpers, co-hosts cannot enter rooms on their own.
- Somebody asking for help gets assigned to a room together with a helper.
- TODO: is it possible to create breakout room for only some participants,
  leaving other learners unaffected? This is crucial for helping participants
  during exercises who have raised their hand. Need to test this
- Host and co-hosts can join any room and jump between rooms. This should be
  used during collaborative exercises to see how the exercise is progressing
  or participate in the group work.
- When a collaborative exercise is about to end, the host/co-hosts can
  broadcast a message into all groups.
- When the host/co-hosts end a breakout room session, participants in groups
  have 60 seconds to finish before the session terminates.


## Exercises

- Just like in a regular workshop, demonstrations and type-along sessions
  should be interspersed with frequent exercises
- For pairwise or group work exercises, the instructor (or Zoom assistant)
  should create breakout rooms with chosen number of participants in each
- For single-person exercises, no breakout rooms are needed
- Learners should be instructed to raise their hand when they need help.
  This corresponds to putting up a red sticky note in in-person workshops.
- TODO: what signal should be used for green sticky notes?
- Polling can be used as formative assessment questions. The host creates
  a poll based on a lesson template and requests learners to answer.
  (TODO: polling seems not available in kth-se zoom subscription)


## Breaks

Following an online event can be even more tiring than a physical event and
therefore also during online sessions we need to plan for breaks as we would
for an in-person event.


## More resources

- <https://foundation.mozilla.org/en/blog/tips-make-your-zoom-gatherings-more-private/>
