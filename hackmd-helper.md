# HackMD helpers

We have one person who is a "HackMD helper".  This isn't the only
person that should edit and answer, but one person shouldn't have too
much else on their mind so can focus on it.  They also make sure that
HackMD is updated with exercise, break, and other meta-information to
keep people on track.

Below, (*) = important.

## Before the workshop

* Create a new hackmd for the workshop
* make sure that **editing is enabled for anyone without login**
* Add workshop information, links to the workshop page and material 
and an example question and answer to the top of the hackmd (see below)

## Most things to edit (everyone)

Make it easy to post after the course and consistent to follow:

* Tag all names with `[name=XXX]` (so they can be removed later),
  remove other personal data or make it obvious.
* Add in information on exercises (new section for them, link, end
  time, what to accomplish)
* Make a logical section structure (`#` for title, `##` for sections,
  `###` for episodes, etc. - or what makes sense)



## General HackMD practices

Keep it formatted well:

- (*) Tag names you see with `[name=XXX]` so that we can remove it later.
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


Update with meta-talk, so that learners can follow along easily:

- Add Icebreaker and introductory material of the day.  Try to talk to
  people as they joined to get them to open HackMD and answer.
- Anything important for following along should not be only said via
  voice.  It needs to be in the HackMD, too.
- New lessons or episodes, with links to them.
- For exercises, link to exercise and add the duration, end time,
  goals.  If these are unclear, bring it up to the instructor by voice.
- Add a status display about breaks.


Screenshare it when necessary:

- During breaks and other times, share the HackMD (including the
  notification about break, and when it ends).
- It is nice if the arrangement allows some of the latest questions to
  be seen, so people are reminded to ask there.
- Someone else may do this, but should make sure it happens.

Answer questions

- If there is an question that should be answered by the instructor by
  voice, bring it up (by voice) to the instructor immediately.
- During breakout sessions, watch for HackMD notifications about
  breakout rooms that need help
  and direct someone to that room.
- How soon do you answer questions? Two points of view:
  - Answer questions right away: can be really intense to follow.
  - Wait some so that we don't overload learners: reduces the info
    flow.  But then do people need to check back more often.
  - You need to find your own balance.  Maybe a quick answer right
    away, and more detailed later.  Or delay answers during the most
    important parts of the lecture.
- Be careful that you don't give too long and involved answers, which
  take up too much mental energy from learners while they are
  learning.  It's a balance you should think about on your own.
  - Here, it is useful to have multiple short followups in bullet
    points, each going a bit more in detail.

Ensure it can be posted quickly:

- HackMD gets posted to the workshop webpage.  For this, it needs some
  minimal amount of formatting (it doesn't need to be perfect, just
  not horrible).
- All names and private information needs to be stripped.  This is why
  you should rigorously tag all names with `[name=XXX]` so they can be
  removed (see above).
  - Learner names can be completely removed.  CR staff names can be
    `[name=CR]` or something similar.
  - There may be other private URLs at the top or bottom.

- If possible, send the PR adding the HackMD to the workshop webpage
  (though others can do this, too).



## HackMD format example

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

## Posting HackMD to website

HackMD should be posted sooner rather than later, and hopefully the
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
