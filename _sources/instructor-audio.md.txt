# Instructor audio

Audio quality, and balance between instructors, is *absolutely
critical* to good online work, especially teaching.  Consider the
following:

## Checklist

* Can you adjust your microphone volume from very low to
  higher-than-needed?  Make sure your dynamic range is larger than
  "barely working", so that you have some room to adjust for later.
* Do you have a high-quality headset?  A headset with microphone is
  the most reliable, but if you can get a desktop setup working
  well, that can be good too.  Always have a high-quality headset for
  backup anyway.

  * If you don't, and are employed to do CodeRefinery teaching, ask
    your employer to provide you a headset meeting these criteria.

* If you have a bluetooth headset, consider:

  * Bluetooth headsets have significant latency compared to wired or
    purpose-built wireless protocols like gaming headsets have.
  * The microphone might not have enough bandwidth (if it's part of
    the same headset).
  * Bluetooth 5 is much better in both latency and quality.
  * Consider investing (or getting your work to invest in) some
    high-quality headset or desktop audio gear.
  * **Recommendation: Don't use a bluetooth headset.  Tell your
    employer you need something for meetings.**

* "Ducking" is when the first words are silenced/quieted by noise
  cancellation, until it detects speaking.  To avoid this, don't use
  "high" noise cancellation (as low as possible is better, reduce
  environmental noise / use headset mic instead).  If you
  need high cancellation because of background noise, switch to your
  headset.
* Set your microphone's hardware volume to something relatively high -
  and control via the software.


## Latency tester

You can use this web app latency tester
<https://nullvoxpopuli.github.io/latency-tester/> to check your
headset's latency.

* Use the tester.  Try to click the button in sync with the beats.
  You'll be delayed in the first few beats, but will soon sync up and
  after 10 beats you'll get an accurate reading.
* Target values
  * A good value for wired headphones is less than 50ms (it can be
    within the margin of error of zero!).
  * A good value for low-latency wireless (dedicated dongle) is
    100-200ms
* Other example values
  * 1000-1500ms: The 100-200ms headphones also have a high-quality,
    high-latency mode when the microphone is not being captured.  The
    latency is over one second.

* Just consider the difference now, between having a discussion with
  someone and having 1.5s round-trip latency between compared to 200ms
  round-trip latency (adding some for Zoom latency - which can be
  quite small on good connections).
