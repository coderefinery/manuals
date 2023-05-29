# Instructor technical setup, online

```{seealso}
This is online-specific instructor tech setup.  For general, see
{doc}`instructor-tech-setup` which also applies here.
```

The information in this is currently specific to Zoom teaching and
livestream teaching.

```{admonition} Final checklist

See the list in {doc}`instructor-tech-setup`, which includes points for
online.
```

## Audio

Audio quality is one of the most important things for quality.

* Can you adjust your microphone volume from very low to
  higher-than-needed?  Make sure your dynamic range is larger than
  "barely working", so that you have some room to adjust for later.
* Do you have a high-quality headset?  If you can get other
  microphones that work without echo, but a headset is worth it for
  back-up.
* If you have a bluetooth headset, consider:

  * Bluetooth headsets have significant latency compared to wired or
    purpose-built wireless protocols like gaming headsets have.
  * The microphone might not have enough bandwidth (if it's part of
    the same headset).
  * Bluetooth 5 is much better in both latency and quality.
  * Consider investing (or getting your work to invest in) some
    high-quality headset or desktop audio gear.



## Screen sharing

You have to assume the smallest screen from learners and plan for
that.  You should share a **portrait** screen: either a portion of
your screen, or one window in portrait mode.  See the examples below.

- Learners have a small screen, and need room for their own terminals
  and web browser open, too.  A big screen or multiple monitors is
  the special case.
- Sharing a 1920x1080 screen is not a good idea: you need to make all
  the text size large so that learners can scale it down to have room
  to do their work.  Pixels are wasted.  **Instead, force yourself to
  save space by using a normal font size but sharing less of your
  screen.**
- Zoom now has a "share portion of screen" (Screen sharing → Advanced
  → Share a portion of the screen).
- For livestreaming, our aspect ration is 840×1080 (**portrait**).
  This is a bit less than half your screen.  This is 43% of the width
  of your screen and the full height, for a standard FullHD screen.

When streaming/recording: **Never stop sharing a screen, ask someone
else to take it over**.
There is a chance that the view goes to "gallery view" in the
recording or stream, which makes video editing harder or disrupts
learner privacy.



### Screen share examples

These are layouts of the actual screen or portion of screen being
shared:

```{figure} img/instructor-tech-online/screenshare-fullhd.png
:width: 75%

**S1**: A FullHD 1920x1080 screen shared.
```

```{figure} img/instructor-tech-online/screenshare-vertical.png
:width: 50%

**S2**: A vertical screen layout shared.  Note the extra shell history at the
top.  The web browser is at the bottom, because the Zoom toolbar can
cover the bottom bit.
```

```{figure} img/instructor-tech-online/screenshare-jupyter.png
:width: 50%

**S3**: A sort-of GUI (Jupyter) shared vertically.
```

```{figure} img/instructor-tech-online/screenshare-rsh.png
:width: 75%

**S4**: This isn't a screenshare from CodeRefinery, but may be instructive.
Note the horizontal layout and shell history at the bottom right.
```

```{figure} img/screenshare/s5-shell-intro-dark.png
:width: 75%

**S5**: Similar to above, but dark.  Includes contents on the right.
```

```{figure} img/screenshare/s8-modular-code-development.png
:width: 50%

**S8**: Jupyter + terminal, including the ``fish`` shell and the
terminal history.
```

```{figure} img/screenshare/s9-git-intro.png
:width: 50%

**S9**: Similar to S8.  Lesson + terminal, ``tmux`` plus terminal history
and dark background.
```

```{figure} img/screenshare/s10-kickstart-prompt-log.png
:width: 50%

**S10**: HPC Kickstart course.  Note the colors contrast of the
windows and colors of the prompt and text.  The history is smaller and
doesn't take up primary working space.  The working directory is
in the window titlebar.
```


### Screen layout: learners

This is how learners can arrange their screen:

```{figure} img/instructor-tech-online/learner-largescreen.png
:width: 75%

**L1**: Learner with a large screen, Zoom in dual-monitor mode so that the
instructur pictures are not shown.  Screenshare is on the left side,
HackMD at bottom left, terminal and web browser on the right.
```

```{figure} img/instructor-tech-online/learner-normal.png
:width: 75%

**L2**: A learner with a single large screen (Zoom in "single monitor mode").
Instructor screen share at right, learner stuff at left.
```

```{figure} img/instructor-tech-online/learner-small.png
:width: 75%

**L3**: A learner with a particularly small screen.  Instructur screenshare at
left, your windows at right.
```

## Screen layout: instructors

This is what the instructor sees on their screen:

```{figure} img/instructor-tech-online/instructor.png
:width: 75%

**I1**: Vertical instructor setup.  Zoom is sharing a portion of the left
side, the right side is free for following HackMD, chat, etc (but
don't overload yourself).
```
