# Instructor technical setup

## Technical

- Move your `.bashrc` and `.gitconfig` files to somewhere else before
  you begin.  You want your environment to match the student's as
  closely as possible. Consider setting `export PS1="\w $ "` in terminal.

- Create a nice, large shell window with good contrast on the screen.
  Beware of colorized text, such as the red in "git diff".

- Make sure the text is more than large enough - people are not just
  reading, but struggling to find the important parts.


## Screencasting

Set an easily-viewable prompt.  Colors may be good, or if not have a
newline (don't little minimal color and no spacing between commands,
it is hard to parse what's a command and what's an output.)  The
minimum is `export PS1='\n\w \$ '`.  With color is `export
PS1='\n\[\e[0;36m\]\w \$\[\e[0m\] '`.

If you are doing live shell work, you will have commands and output
all interleaved, which makes it hard to follow what you actually
typed.  Have a separate window that shows recent commands only,
without output.  Arrange your screen so there is the main window and
the smaller "history" window.  The history window runs the tail
commands and can be used as a reference for what you just did.


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
