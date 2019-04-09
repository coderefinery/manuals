# Lesson presentation hints.

This is a checklist/hints on what to do when standing up and giving a
presentation... more local than the [workshop administration
page](workshop-administration.md).


## Before each lesson

### Non-technical

- Remember: sticky notes, water

- Make your text large enough to be seen in the back, then bigger.
  Make your voice loud enough to be heard in the back, then louder.


### Technical

- Move you `.bashrc` and `.gitconfig` files to somewhere else before
  you begin.  You want your environment to match the student's as
  closely as possible.

- Create a nice, large shell window with good contrast on the screen.
  Beware of colorized text, such as the red in "git diff".

- Make sure the text is more than large enough - people are not just
  reading, but struggling to find the important parts.


## Screencasting

If you are doing live shell work, you will have commands and output
all interleaved.  Have a separate window that shows recent commands
only, without output.  The simple way is `PROMPT_COMMAND="history -a"`
and then `tail -f .bashrc`, but this: doesn't capture ssh, subshells,
and only shows the command after it is completed.

Also check the [shell exporter by
sabryr](https://github.com/Sabryr/Teaching-aids), which copies recent
history to a remote server.

Arrange your screen so there is the main window and the "history"
window.  The history window runs the tail commands and can be used
as a reference for what you just did.

**Easy method**: Set `PROMPT_COMMAND = "history -a"` and in another window, run `tail
-f -n 0 ~/.bash_history`  (these commands have not been checked).  Show a
few lines of the tail window at the top of the screen, above your main
shell window.  Now, the students can see your last few commands, even
if they scroll off the screen and without having to search for your
prompt.  The disadvantage is that the prompt is only written after the
command terminates.

**Advanced**: Below are more advanced commands.  These might work but needs
debugging (there are lots of complexities in extracting out the right
parts), but will get commands as soon as they are run and also will
capture commands if you `ssh` to somewhere else, etc.  Note: this
begins working after the second line you type, somehow.

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

# used for the fish shell (note: untested)
tail -f -n 0 ~/fish_history | sed -u -e s'/- cmd:/ \>/'
```


## Starting off

- Don't start off with tech details, say why this is important.  Think
  of what the emotional ("coolness") appeal is and start off with
  that.
- Why will this be useful?

## Team teaching

- Discuss with co-teachers and helpers about what each of you will do.



## Wrap up

- Say what you taught and why.
- Say what comes next.  Say where to get that.
- Update the instructor's guide and file issues for any problems you
  noticed.
- Get instant feedback from your co-teachers and helpers (students
  too, if they offer any).
