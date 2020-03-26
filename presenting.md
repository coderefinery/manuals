

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

- Have a pen and paper next to you.  When you notice problems in the
  material, write it down right away during breaks in the type-along
  parts.

- Set up feedback system (chat, questions, etc)


### Technical

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
- Encourage the use of sticky notes (red=need help, green=I am done with the
  solution). They can also be used for voting, e.g. red/green for two
  answers of a multiple choice question.
- Don't touch the learner's keyboard!  This is very hard to do, since
  it's only natural to want to get things done quickly.  The best idea
  we have is to have a pen and sticky notes, when it's hard to spell
  out a command to type, write it instead.
- If appropriate for your topic, create a cumulative
  cheatsheet/diagram on the board as you are presenting.
- Take advantage of the mistakes/typos you make when teaching!
  When you do a mistake and get an error message and realize what you did wrong,
  explain what happened since this can offer valuable insights to learners.
- Ask "do you do X?" where X is what you are teaching.  Instead, ask
  "how do you do Y?".  The first question implies something you are
  doing wrong, the second is open-ended.


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
