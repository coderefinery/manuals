

# Lesson presentation hints.

This is a checklist/hints on what to do when standing up and giving a
presentation.


## Before each lesson

### Non-technical

- Remember: sticky notes, water, extra whiteboard markers.

- Make your text large enough to be seen in the back, then bigger.
  Make your voice loud enough to be heard in the back, then louder.

- As people are coming in, encourage them to sit next to someone with
  a similar operating system - then, when helping each other, the
  unimportant differences are minimized.

- By the same token, don't allow people to sit alone: ask everyone to
  set next to at least one other person.  That way, people can help
  each other.

- Set up feedback system (chat, questions, etc)


### Technical

- Move your `.bashrc` and `.gitconfig` files to somewhere else before
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
and then `tail -f .bashrc`, but this doesn't capture ssh, subshells,
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
  - Hand signals for common situations: too fast/slow in general,
    louder, time for a break, "good enough, move on", "explain more
    here".
- It can be hard for one person to manage everything.  How can
  multiple instructors take part?  Probably the most common ones are:
  - Teach teaching: alternating
    - Commander and navigator: conceptually divide roles of big
      picture teaching and doing the details.
	- If "real" alternating, each section should be 10-15 min at
      least, otherwise too much context switching is distracting.
  - Teach and assist (master helper going around)
  - Teach and observe.
  - Asking directed questions to fill in gaps.
- Tell the students the way the teachers will work together, so that
  it seems coordinated rather than someone is interrupting.


## During the lessons

- Helpers can read [the helping and teaching guide](helping-and-teaching.md).
  Encourage helpers to stand and be
  constantly walking around, people rarely flag helpers from across
  the room.
- Encourage the use of sticky notes.  They can also be used for
  voting, e.g. red/green for two answers of a multiple choice
  question, red=need help, green=I am done with the solution.
- Don't touch the learner's keyboard!  This is very hard to do, since
  it's only natural to want to get things done quickly.  The best idea
  we have is to have a pen and sticky notes, when it's hard to spell
  out a command to type, write it instead.
- If appropriate for your topic, create a cumulative
  cheatsheet/diagram on the board as you are presenting.


### Try to stick to the material

- Don't try to show everything, show less, but show it clearly.
- Try not to completely deviate from the material. Ideally, rather influence the material before you teach.
  Of course it is good to react to questions and to adapt the material to the audience, so sometimes an excursion can be very useful,
  but make clear that you then deviate from the script
  and be explicit about whether participants should follow what you do or only watch.
- If you want to show some extra steps in the terminal, show them perhaps at the end of an exercise block to not
  "mess up" the exercise half-way and change it with respect to the material.
- It is good to mention an anecdote or two but be careful about mentioning too much new jargon which
  only very few participants may relate to.


## Wrap up

- Say what you taught and why.
- Say what comes next.  Say where to get that.
- Update the instructor's guide and file issues for any problems you
  noticed.
- Use the sticky notes to get good/bad feedback: have people write one
  good and one to be improved thing, and leave the note on the door on
  the way out.
- Get instant feedback from your co-teachers and helpers (students
  too, if they offer any).
  - Consider making notes on a 4-way diagram of
    (content←→presentation) × (went well←→can be improved).
