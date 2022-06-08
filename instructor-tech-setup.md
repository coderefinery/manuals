# Instructor technical setup

```{seealso}
* {doc}`instructor-tech-online`
```

Appearance matters.  When you look at other professionally made videos
online, they look good.  As a presenter, you also need to work to make
your screen look pleasing to the eye.  As a teacher of tech, you also
*need to make sure that your screen supports the learning process*:
you have conflicting goals of:

* Making your screen look simple, to not distract from what you are
  trying to teach, and
* Showing more advanced practical setups that others may want to copy.

In general, try to use a simpler arrangement at the beginning of
workshops.  You, or other teachers, can begin showing more advanced
screen layouts once learners are able to see what is important and
what is extra.



## Check with someone before you start teaching

**Most importantly, get your setup done well in advance and show your
co-teachers for feedback.  Feedback and time to improve is very
important to make things beautiful.**



## Clean your environment

Do you have fancy ``.bashrc``, ``.gitconfig``, etc files?  Move them
away so that you are as plain and normal as possible - beyond
appearances, you don't want to use any shortcuts that every learner
won't have access to ("hint: configure this" isn't enough, those who
miss this will still be lost).

Relevant files:

* ``.bashrc``
* ``.gitconfig``
* ``.ssh/config``, ``.ssh/authorized_keys``
* ``.conda/*``
* Any config for any program you may demonstrate


## Command line prompt

Learners have to read your prompt quickly, understand what you
entered, copy it, all the while not being distracted by everything
else or your screen.  Set an easily-viewable prompt.

- Colors may be good, or if not have a newline (don't little minimal
  color and no spacing between commands, it is hard to parse what's a
  command and what's an output.)

- Consider prompt-log by rkdarst
  (https://github.com/rkdarst/prompt-log).  It adds a interesting idea
  that *the command you enter is also in color* and also provides
  terminal history *before the command returns* (see below).  This is
  still in development.

- The minimum is `export PS1='\n\w \$ '` or even `\$ `.

- With color is `export PS1='\n\[\e[0;36m\]\w \$\[\e[0m\] '`.

- Consider setting `export PS1="\w $ "` in terminal (see below for
  more), especially the first day.

- See below for more prompt configuration


## Terminal appearance

- Create a nice, large shell window with good contrast on the screen.
  Beware of colorized text, such as the red in "git diff".

  - Consider setting a profile for your terminal, pre-configured for
    courses (e.g. white, large size, dark colors).

  - Eliminate menu bars and any other decoration that uses valuable
    screen space.

  - Know and use keyboard shortcuts for changing the font size.  You
    can be larger when you are doing simple things, and make it
    smaller when you have long lines that learners need to see.

- Don't clear terminal often (or ever).  Learner's can follow as fast
  as you!  More people will wonder what just got lost than are helped
  by seeing a blank screen.  Consider pushing ``ENTER`` a few times
  instead.

## Optimize any other applications

Adjust any other applications to appear "normal" and minimize wasted
space.  For example, an advanced things to do would be minimize the
size of title bars, remove menu bars when not needed, or reduce the
size of tabs in web browsers.



## Command line history

You *need* to find a way to show the recent commands you have entered,
outside of your main window, so that learners can see the recent
commands.

If you are doing live shell work, you will have commands and output
all interleaved, which makes it hard to follow what you actually
typed.  Have a separate window that shows recent commands only,
without output.  Arrange your screen so there is the main window and
the smaller "history" window.  The history window runs the tail
commands and can be used as a reference for what you just did.

- Ideally, commands will appear before they terminate (if you ``less
  file``, the command should appear before ``less` returns).

Consider prompt-log by rkdarst
(https://github.com/rkdarst/prompt-log), which gives colors and
history even before the command returns.

Also check the [shell exporter by
sabryr](https://github.com/Sabryr/Teaching-aids), which copies recent
history to a remote server.

**Simple**: The simple way is `PROMPT_COMMAND="history -a"` and then
`tail -f -n0 ~/.bash_history`, but this doesn't capture ssh,
subshells, and only shows the command after it is completed.

**Better yet still simple**: Many Software Carpentry instructors use
[this script](https://github.com/rgaiacs/swc-shell-split-window),
which sets the prompt, splits the terminal window using tmux and displays command history
in the upper panel. Requirement: [tmux](https://github.com/tmux/tmux/wiki)

**Better (bash)**: This prints the output before the command is run,
instead of after.  Tail with `tail -f ~/demos.out`.

```
BASH_LOG=~/demos.out
bash_log_commands () {
    # https://superuser.com/questions/175799
    [ -n "$COMP_LINE" ] && return  # do nothing if completing
    [[ "$PROMPT_COMMAND" =~ "$BASH_COMMAND" ]] && return # don't cause a preexec for $PROMPT_COMMAND
    local this_command=`HISTTIMEFORMAT= history 1 | sed -e "s/^[ ]*[0-9]*[ ]*//"`;
    echo "$this_command" >> "$BASH_LOG"
}
trap 'bash_log_commands' DEBUG
```

**Better (zsh)**: This works like above, with zsh.  Tail with `tail -f
~/demos.out`.

```
preexec() { echo $1 >> ~/demos.out }
```

**Better (fish)**: This works like above, but for fish.  Tail with
`tail -f ~/demos.out`.

```
function cmd_log --on-event fish_preexec ; echo "$argv" >> ~/demos.out  ; end
```

**Better (tmuxp)**: This will save some typing. [TmuxP](https://tmuxp.git-pull.com/) is a Python program (`pip install tmuxp`) that gives you programmable `tmux` sessions. One configuration that works (in this case for `fish` shell):

```yaml
session_name: demo
windows:
  - window_name: demo
    layout: main-horizontal
    options:
      main-pane-height: 7
    panes:
      - shell_command:
          - touch /tmp/demo.history
          - tail -f /tmp/demo.history
      - shell_command:
          - function cmd_log --on-event fish_preexec ; echo "$argv" >> /tmp/demo.history  ; end
```

**Windows PowerShell**: In [Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/),
a split can be made by pressing `CTRL+SHIFT+=`. Then, in one of the splits, the following
PowerShell command will start tracking the shell history:
```
Get-Content (Get-PSReadlineOption).HistorySavePath -Wait
```
Unfortunately, this only shows commands after they have been executed.

**Obselete**: The below commands rely on recording your entire session
using `script`, and then dynamically following the output.  This
allows you to track commands even in subshells/over ssh, but introduce
a lot of other errors in corner cases.  These might work but needs
debugging (there are lots of complexities in extracting out the right
parts).  Note: some of these ignore the first line you type.

```
script -f demos.out

# most general... prompt must end in '$ '.
tail -n 0 -f demos.out | awk '{ if (match($0,/^[^$ ]+ ?[^$ ]*[$][[:cntrl:]0-9m;[]{,10} (.*)/,m)) print m[1] }'

# Prompt format of [username@host]$
tail -n 1 -f demos.out | while read line; do [[ "$line" =~ \]\$\ ([^ ].+)$ ]] && echo  ${BASH_REMATCH[1]}; done

# Standard bash prompt of 'user@host$ ' (less likely to have false positives)
tail -n 0 -f demos.out | awk '{ if (match($0,/^[^@]+@[^$]+[$][^ ]* (.*)/,m)) print m[1] }'

# Prompt is $ ' alone on a line.
tail -n 0 -f demos.out | awk '{ if (match($0,/^[$] (.*)/,m)) print m[1] }'
```

```
# used for the fish shell (note: untested)
tail -f -n 0 ~/fish_history | sed -u -e s'/- cmd:/ \>/'

# used for zsh shell (put this into a script file)
clear >$(tty)
tail -n 0 -f ~/.zsh_history | awk -F\; 'NF!=1{printf("\n%s",$NF)}NF==1{printf("n %s ",$1)}'
```
