# Notes manager

The "Notes" are the way we communicate in the workshop.  We have a
manager for them.  This isn't the only person that should edit and
answer, but hopefully one person can focus on it each day of the
workshop.  They make sure it stays up to date when others may be too
busy managing other things.

"Notes" used to be called "HackMD" (or "collaborative document").  To
be consistent, please call it "Notes".

Below, (*) = important.



## Before the workshop

* Create a blank notes document and fill it with the template.
* Create a archive place on HackMD to store the overflow.  This should
  be writeable only by owners.
* Make sure that **editing is enabled for anyone without login**
* Add workshop information, links to the workshop page and material 
  and an example question and answer to the top of the hackmd (see below)


## General practices (for everyone)


```{figure} img/hackmd--full-demo.png
:align: right

A live demo of Notes during a Q&A time.  The two instructors are
discussing some of the import answers.  Multiple learners have asked
questions, multiple answers, and some remaining to be answered
```

Keep it looking good so that it's easy to post after the course and
consistent:

* Remove all names or at least tag them with `[name=XXX]` (so they can
  be found and removed later), and remove other personal data.
* Add in information on exercises, breaks, etc (new section for them, link, end
  time, what to accomplish)
* Make a logical section structure (`#` for title, `##` for lessons,
  `###` for episodes, etc. - or what makes sense)



Keep it formatted well:

- (*) Tag names you see with `[name=XXX]` so that we can remove it
  later.
- Heading level `#` is only the page title
- Add a new `##` heading when a new *lesson* or similar thing is
  started (introduction, icebreaker, break between lessons, etc)
- Add a new `###` heading when a new *episode*, *exercise*, *break*
  (within exercise session)
- Ensure people are asking questions at the bottom, direct them there
  if they aren't.
- (*) Ensure each question is a bullet point.  Each answer or follow-up
  should be a bullet point below.
  - Should you use more deeply nested bullet points, or have only one
    level below the initial question?  It depends on the context, but
    if a conversation goes on too long, try not to let it go too
    deep.
- If using numbered questions, leave a blank line between numbers (so
  that pushing enter after a line doesn't increment following
  numbers).

Update with meta-talk, so that learners can follow along easily:

- Add Icebreaker and introductory material of the day.  Try to talk to
  people as they joined to get them to open the Notes and answer.
- Anything important for following along should not be only said via
  voice.  It needs to be in the Notes, too.
- New lessons or episodes, with links to them.
- For exercises, link to exercise and add the duration, end time,
  goals.  If these are unclear, bring it up to the instructor by voice.
- Add a status display about breaks.

Screenshare it when necessary:

- During breaks and other times, share the Notes (including the
  notification about break, and when it ends).
- It is nice if the arrangement allows some of the latest questions to
  be seen, so people are reminded to ask there.
- Someone else may do this, but should make sure it happens.

Answer questions:

- If there is an question that should be answered by the instructor by
  voice, bring it up (by voice) to the instructor immediately.
- During breakout sessions, watch for Notes notifications about
  breakout rooms that need help
  and direct someone to that room.
- How soon do you answer questions? Two points of view:
  - Answer questions right away: can be really intense to follow.
  - Wait some so that we don't overload learners: reduces the info
    flow.  But then do people need to check back more often.
  - You need to find your own balance.  Maybe a quick answer right
    away, and more detailed later.  Or delay answers during the most
    important parts of the lecture.
- Avoid wall-of-text answers.  If reading an answer takes too long, it
  puts the person (and other people who even try to read it) behind
  even more by taking up valuable mental energy.  If an answer needs a
  wall of text, consider these alternatives:
  - Progressive bullet points getting more detailed (first ones
    useful alone for basic cases)
  - Don't be worried to say "don't worry about this now, let's talk
    later."
  - Figure out the root problem instead of answering every possible
    interpretation
  - Declare it advanced and that you will come back later.

Archive if it gets too long:

- If it gets too long, the interaction starts lagging.  In this case,
  copy old material (generally everything before the current
  episode/lesson and possibly the previous one) to the archive
  document.  Make sure it's linked at the top.

Ensure it can be posted quickly:

- Notes gets posted to the workshop webpage.  For this, it needs some
  minimal amount of formatting (it doesn't need to be perfect, just
  not horrible).
- All names and private information needs to be stripped.  This is why
  you should rigorously remove or tag all names with `[name=XXX]` so
  they can be removed (see above).
  - Learner names can be completely removed.  CR staff names can be
    `[name=CR]` or something similar.
  - There may be other private URLs (e.g. Github repo links).

- If possible, send the PR adding the Notes to the workshop webpage
  (though others can do this, too).



## Notes format example

```
# Workshop, day 1


## Lesson name
https://coderefinery.github.io/lesson/

### Episode name
https://coderefinery.github.io/01-episode/

- This is a question
  - Anwser
  - More detailed answer
- question
  - answer

### Exercises:
https://link-to-exercise/.../.../#section
20 minutes, until xx:45
Try to accomplish all of points 1-3.  Parts 4-5 are optional.

Breakout room status:
- room 2, need help with Linux permissions
- room 5, done

### Break
:::danger
We are on a 10 minute break until xx:10
:::


## Lesson 2
https://coderefinery.github.io/lesson-2/

```

## Posting Notes to website

Notes should be posted sooner rather than later, and hopefully the
steps above will make it easy to do so quickly.  You could wait a few
hours, to allow any remaining questions to be asked an answered.

- Download as markdown
- Remove any private links at the top
- Adjust headings so that they are reasonable
- Look for private info and remove it
  - Search document for `[name=???]`  (change to `[name=staff]` or
    `[name=learner]`)
  - Any names not tagged with `[name=]`
  - usernames in URLs
  - private links

## Feedback template

``````
## Feedback, day N

:::info
### News for day N+1
- .
- .
:::

### Today was (multi-answer):
- too fast: 
- just right: 
- too slow: 
- too easy: 
- right level: 
- too advanced: 
- I would recommend this course to others: 
- Exercises were good: 
- I would recommend today to others: 
- I wouldn't recommend today: 

### One good thing about today:
- ...
- ...

### One thing to be improved for next time:
- ...
- ...

### Any other comments:
- ...
- ...
``````
