Please improve these notes with issues and pull requests.


# Pre-workshop

- Announce registration
- Email persons who registered to notify-me form
- Maintain waiting list if needed
- Make sure schedule makes sense and that instructors know session durations
- Send out install instructions one week ahead, also ask those without Eduroam to speak up
- Organize sticky notes
- Organize catering
- Organize extension cables if needed
- Organize alternative wireless for those without Eduroam (if any)
- Prepare a shared Google doc with global write permissions, consider creating a memorable short-link


# Repositories that require --force clean-up before the sessions

- Collaborative Git requires resetting https://github.com/coderefinery/centralized-workflow-exercise and https://github.com/coderefinery/forking-workflow-exercise

# As people arrive

- Emphasize to people that you need to sit with someone - don't work alone.
- Try to have people sit next to someone with a simliar operating
  system if they have no preference, since they will face similar
  problems.

# Introduction talk

- Welcome
- Quick background on CodeRefinery and NeIC
- Brief presentation of instructors and helpers
- Brief presentation of participants
- Installation issues?
- Mention GitLab service
- Brief program walkthru
- Mention that all material is online and CC-BY-SA
- Welcome contributions to the material (issues or pull requests)
- Advertise opportunities to contribute as helper or instructor at future workshops
- Explain teaching style and sticky notes visual feedback
- Encourage (optional) session feedback (one aspect you enjoyed, one aspect we need to improve)
- Announce that there will be a 6 months feedback that will take 5 minutes time to complete
- Check access to electricity
- Check wireless connectivity
- Announce coffee breaks (if any)
- Encourage social media but give participants option to not appear anywhere
- Encourage sharing links and asking also in shared document
- Collect lunch options in shared document

# Before each lesson

- Move you `.bashrc` and `.gitconfig` files to somewhere else before
  you begin.  You want your environment to match the student's as
  closely as possible.

- Create a nice, large shell window with good contrast on the screen.
  Beware of colorized text, such as the red in "git diff".

- Make sure the text is more than large enough - people are not just
  reading, but struggling to find the important parts.

- Show your shell history in a separate window, so that students can
  see the last few commands you ran without scanning through all of
  the output.

  - Easy method: Set `PROMPT_COMMAND="history -a"` and in another
    window, run `tail f -n 0 ~/.bash_history`.  Show a few lines of
    the tail window at the top of the screen, above your main shell
    window.  This method doesn't work in subshells, ssh, etc. but is
    simple and effective.

  - Advanced method: In your main demonstration window, run `script`
    to record files.  In the history window, run this `tail` command
    which prints just the command out of the history.  Note that the
    regex is rather fragile adn it seems the printing starts on the
    second line only.

    - `script -f demos.out`
    - `tail -n 0 -f demos.out | awk '{ if (match($0,/^[^@]+@[^$]+[$][^ ]+ (.*)/,m)) print m[1] }'`
    - `tail -n 0 -f demos.out | egrep --line-buffered '^[^@ ]+@[^$]+\$'`  (more robust, but shows the whole prompt)

# During workshop

- Keep up interactive feel by encouraging and asking questions
- Keep time
- For presentations which have shell commands, create a
  cheatsheet/reference on the board in real time.
- Remind people about sticky notes.
- Make sure we take regular breaks (at least a short break each hour)
- Give participants some time to also experiment (do not rush the classroom through exercises)
- Encourage optional feedback at the end of each day on sticky notes
- Create GitHub issues for points which are confusing or problematic

# At the end of workshop

- Give credit to those who contributed and helped
- Indicate that we distribute certificates upon request (email and/or paper snail mail)
- Point participants to Twitter and support/discussion channels
- Mention Nordic RSE community


# Post-workshop

- Process and distribute feedback
- Debrief with instructors
- Process certificate requests
