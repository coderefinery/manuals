# Instructor technical setup, online

```{seealso}
This is online-specific instructor tech setup.  For general, see
{doc}`instructor-tech-setup`.
```

The information in this is currently specific to Zoom teaching.

## Screen sharing

You have to assume the smallest screen from learners and plan for that.

- Learners have a small screen, and need room for their own terminals
  and web browser open, too.  A big screen or multiple monitors is
  special.
- Make sure the text is more than large enough - people are not just
  reading, but struggling to find the important parts while the.
- Sharing a 1920x1080 screen is not a good idea: you need to make all
  the text size large so that learners can scale it down, but pixels
  are wasted.
- Sharing a single window would be good, but usually you need more
  than one.
- Zoom now has a "share portion of screen" (Screen sharing → Advanced
  → Share a portion of the screen).
- Our latest idea is:
  - Share a vertical part of the screen, for example half of your
    screen.
  - If you have a FullHD 1920x1080 screen, maybe even a smaller
    portion than that.

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
