# Workshop checklist template

This page is a check list that we use when planning a CodeRefinery workshop
with 300 or more participants.
This is meant to be copied to a HackMD – hence the formatting.

Detailed role descriptions are in the role pages.

> This may be useful in organizing other workshops as well.

Let's keep this brief and copy-paste-able to HackMD/HedgeDoc for the actual planning.

---
# CodeRefinery workshop YYYY-MM-DD

[toc]

## Links

```
- [Workshop page]()
- This document: copy-paste link here from the Share-menu
- [Q&A HackMD]()
- [Archive HackMD]()
- [HedgeDoc Q&A]()
- [Twitch channel](https://www.twitch.tv/coderefinery/about)
- [Emails and communication]()
- [Zoom for onboarding and install help]()
```

:::danger
Add missing links! :arrow_up: 
:::

### Workshop roles

([Overview to the roles behind this link](https://coderefinery.github.io/manuals/roles-overview/))

:::success
**If you want to take part, add your name here, sign up in Indico and select "I am interestest in being a helper, co-instructor, or observer", and you will be contacted.**

#### Instructors
([Description](https://coderefinery.github.io/manuals/instructors/#instructors))

Two names per lesson, first is primary

- [ ] day 1 - git-intro:                ???, ???
- [ ] day 2 - git-intro:                ???, ???
- [ ] day 3 - git-collab:               ???, ???
- [ ] day 4 - reproducible research:    ???, ???
- [ ] day 4 - social coding:            ???, ???
- [ ] day 5 - jupyter:                  ???, ???
- [ ] day 5 - documentation:            ???, ???
- [ ] day 6 - testing:                  ???, ???
- [ ] day 6 - modular code development: ???, ???


#### Learner Zoom team leaders
([description](https://coderefinery.github.io/manuals/team-leaders/))

These are not needed if the teams are formed before the workshop starts and they bring their own team leaders.

#### Expert helpers
([description](https://coderefinery.github.io/manuals/expert-helpers/))

If Zoom: Help in our learner zoom, circle around breakoutrooms; there will probably be 2 or 3 rooms where we need to provide the helper. At least two for each day
  Else: Help answering questions in Collaborative Q&A document.

- [ ] day 1 - git-intro:                ???, ???, ...
- [ ] day 2 - git-intro:                ???, ???, ...
- [ ] day 3 - git-collab:               ???, ???, ...
- [ ] day 4 - reproducible research:    ???, ???, ...
- [ ] day 4 - social coding:            ???, ???, ...
- [ ] day 5 - jupyter:                  ???, ???, ...
- [ ] day 5 - documentation:            ???, ???, ...
- [ ] day 6 - testing:                  ???, ???, ...
- [ ] day 6 - modular code development: ???, ???, ...

#### HackMD manager
([description](https://coderefinery.github.io/manuals/hackmd-helper/#hackmd-manager))

Keep HackMD organized, check for unanswered questions, and archive notes each day.

- [ ] preparation before workshop: 
- [ ] day 1 - git-intro:                ???, ???, ...
- [ ] day 2 - git-intro:                ???, ???, ...
- [ ] day 3 - git-collab:               ???, ???, ...
- [ ] day 4 - reproducible research:    ???, ???, ...
- [ ] day 4 - social coding:            ???, ???, ...
- [ ] day 5 - jupyter:                  ???, ???, ...
- [ ] day 5 - documentation:            ???, ???, ...
- [ ] day 6 - testing:                  ???, ???, ...
- [ ] day 6 - modular code development: ???, ???, ...

:::

### Workshop organization; roles "behind the scenes"

Organiser roles and their responsibilities. This does not mean that a person will do
everything that is part of their responsibility, but they will make sure that
their responsibilities are followed-up and not forgotten.

#### Event director
([description](https://coderefinery.github.io/manuals/director/))
- lead: 
- backup:

:::spoiler Checklist
- Before workshop
  - [x] Create planning HackMD by copying this page to a new HackMD in [CodeRefinery HackMD](https://hackmd.io/team/coderefinery)
  - [x] Distribute roles using the planning HackMD
    - [x] Ask collaborators/stakeholders to pick roles
  - [x] Add all sessions to [CodeRefinery calendar](https://github.com/coderefinery/calendar) separately
  - [x] Send calendar invite to all organizers, instructors, expert helpers, with all relevant links
  - [ ] Decide if certificates will be possible and what is needed for getting a certificate/credits (ask from partner universities)
  - [x] Remind co-organizers to register
- After the workshop:
  - [x] Summarize lessons learned and make it a blog post in [coderefinery.org repo](https://github.com/coderefinery/coderefinery.org)
  - [ ] Coordinate post-workshop survey eg. in Indico
  - [ ] :bulb: Merge new edits from here (no names ofc) to the [Playbook](https://github.com/coderefinery/manuals/blob/master/workshop-playbook.md)
  - [ ] Port changes from workshop page to [template page](https://github.com/coderefinery/template-workshop-webpage)
  - [ ] On CR website move from ["upcoming"](https://github.com/coderefinery/coderefinery.org/blob/main/content/workshops/upcoming.md) to ["past"](https://github.com/coderefinery/coderefinery.org/blob/main/content/workshops/past.md)
  
:::

#### Registration coordinator
([description](https://coderefinery.github.io/manuals/registration-coordinator))
- lead: 
- backup:

:::spoiler Checklist without CR ZOOM
- **ca. 2 months before = When workshop details are set:**
  - [ ] Create [Indico registration page](https://indico.neic.no/category/5/) for the event
    - [ ] Include event information
    - [ ] Customise the registration form
    - [ ] Customise the confirmation email (with outreach and marketing coordinator)
      - [ ] Incl. Zoom link if any
      - [ ] Point to workshop page
      - [ ] Incl. HackMD link if any
  - [ ] Set up a workshop page from [template page](https://github.com/coderefinery/template-workshop-webpage)
  - [ ] Add workshop to ["upcoming courses"](https://github.com/coderefinery/coderefinery.org/blob/main/content/workshops/upcoming.md)
  - [ ] Draft email templates
    - [ ] Registration confirmation email
    - [ ] Info to instructors (with instructor coordinator)
    - [ ] Info to observers (with instructor coordinator)
    - [ ] Info to team leads (with exercise coordinator)
    - [ ] Info to participants (with outreach and marketing coordinator)
      - Remember to add all the emails to workshop page
  - [ ] Open the registration 
  - [ ] Remind instructors and co-organizers to also register for workshop
- **Every day: **
  - Check [support email (Freshdesk)](https://coderefinery.zulipchat.com/#narrow/stream/215460-coderefinery/topic/freshdesk.20procedures) for requests/questions
- **Every week: **
  - Check registrations for problems
    - Identify if need to do something – basically, "playing" with the registration data to not forget anybody and not to forget follow-up
  - Update [stats](https://github.com/coderefinery/workshop-stats) 
  - Update workshop-webpage if new local organisations
- **ca. 1 month before:**
  - [ ] Reach out to participants ([examples from Mar 2023](https://github.com/coderefinery/2023-03-21-workshop/tree/main/content/communication))
    - [ ] [Team leaders](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/email-to-team-leads.md) 
    - [ ] [Those who indicated interest in co-organizing and co-teaching](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/email-to-co-org-helpers.md)
    - [ ] [Communicate about self organising teams](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/exercise-teams-2023-03-09.md)
- **Two weeks before**
  - [ ] [Send general information to all](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/practical-info-2023-03-09.md)
    - Next steps, onboarding, installation
    - Those who have a team, please organize your own zoom/video 
  - [ ] [Inform those who want in-person about known LOs](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/local-groups-2023-03-09.md)
  - [ ] Try to match up learners and helpers who want to be part of a team
    - [ ] Send emails to local event organisers Including the contact details of participants in the area for targeted emails.
      - This requires that this data usecase is clearly communicated!
- **ca. 1 week before** 
  - [ ] Update indico auto-reply for last minute registrations
  - [ ] Send [email with all links](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/links-2023-03-15.md)
- **1 day before!**
  - [ ] Send a [reminder with links](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/links-2023-03-20.md)
- **During the workshop**
  - [ ] Send [daily summaries](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/summary-day1.md) (with exercise coordinator)
    - [Some of them have also preparation instructions!](https://github.com/coderefinery/2023-03-21-workshop/blob/main/content/communication/summary-day2%2Bprep-day3.md)
- **After the workshop:**
  - [ ] Add viewing statistics to [CodeRefinery webpage](https://github.com/coderefinery/coderefinery.org/tree/main/content/about/statistics)
    - [ ] Use [statistics repo](https://github.com/coderefinery/workshop-stats) (feel free to edit)
  - [ ] Close registration
:::


#### Broadcaster
([description](https://coderefinery.github.io/manuals/broadcaster/))
- lead: 
- backup:

:::spoiler Checklist
  - [ ] Prepare Ice-breakers for each day (in [learner HackMD](https://github.com/coderefinery/workshop-stats))
  - [ ] Create instructor Zoom and communicates it (with exercise coordinator and outreach and marketing coordinator)
  - [ ] Publish recordings (does not do all the work but coordinates it)
    - [ ] Prepare for upload (use [ffmpeg-editlist](https://github.com/coderefinery/ffmpeg-editlist) and collaborate)
    - [ ] Upload videos and communicate (with outreach and marketing coordinator)
:::


#### Instructor coordinator
([description](https://coderefinery.github.io/manuals/instructors/))
- lead: 
- backup:

:::spoiler Checklist
  - [ ] Confirm that each lesson and session has co-instructors
  - [ ] Schedule calls with each instructor pair to distill most important questions and tasks to them
    - [ ] Show where the detailed schedule is and recommend to move it to instructor guide
    - [ ] Discuss that the detailed schedule can and should be improved
    - [ ] Show where Q&A and feedback from past workshop can be found
    - [ ] Discuss plans for exercises: try 3 exercises each half-day, each not shorter than 20 mins
    - [ ] Ask them to check their lesson's exercise list
    - [ ] Ask for any software requirements changes
    - [ ] Inform about audience (at the time of writing half of registrants prefer to follow on their own) - adapt exercise expectations to audience
    - [ ] Check/test for high-quality screen share 
  - [ ] Inform instructors that they need to register
  - [ ] Send email to Observers and save to website
  - [ ] Instructor briefing: make sure learners get a good experience (lesson material, issues, style, screen share)
  - [ ] Remind instructors to send software install requirements in time
  - [ ] Make sure software install instructions work
  - [ ] List instructors on the website (with exercise coordinator)
  - [ ] Organize team leader On-boarding sessions (with exercise coordinator)
:::


#### Exercise and team leader coordinator
([description](https://coderefinery.github.io/manuals/exercise-coordinator/))
- lead: 
- backup:

:::spoiler Checklist
- **ca. 2 months before = When workshop details are set:**
  - [ ] Create and host exercise Zoom (with instructor coordinator)
    - [ ] Create exercise groups
    - [ ] Provide [practical instructions](https://github.com/coderefinery/template-workshop-webpage/issues/73) in the exercise zoom
  - [ ] Communicate exercise Zoom to paricipants (with outreach and marketing coordinator)
  - [ ] Inform those who we can't accommodate into groups that they can follow stream and need to somehow self-organize
  - [ ] Create learner HackMD (create nice URL) with all relevant links 
    - [ ] Use [CodeRefinery HedgeDoc](https://notes.coderefinery.org) or [HackMD](https://hackmd.io/team/coderefinery)
  - [ ] Draft email templates
    - [x] Registration confirmation email
    - [ ] Info to instructors (with instructor coordinator)
    - [ ] Info to observers (with instructor coordinator)
    - [ ] Info to team leads (with exercise coordinator)
    - [ ] Info to participants (with registration coordinator)
  - [ ] Create/update [advertising texts](https://github.com/coderefinery/template-workshop-webpage/tree/main/content/communication) and relevant news on the workshop page
- **ca. 1 month before:**
  - [ ] Make sure exercise list is communicated (with outreach and marketing coordinator)
  - [ ] List all team leads (who consent to being listed) on the website (with instructor coordinator)
  - [ ] List expert helpers on the website (with instructor coordinator)
- **ca. 2 weeks before**
  - [ ] Make sure that each workshop day has a learner HackMD editor who edits and archives at the end of the day
  - [ ] Organize Staff & Helpers On-boarding sessions (with instructor coordinator)
    - [ ] Communicate to staff + helpers (with outreach and marketing coordinator)
  - [ ] Send team leader onboarding summary email + save it to the website (with outreach and marketing coordinator)
- **After each workshop day**
  - [ ] Draft "summary and preparation for next day" email to all (can be based on the website news and link there so that it can be
    updated)
    - [ ] [EXAMPLE: day 1 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/33)
    - [ ] [EXAMPLE: day 2 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/41)
    - [ ] [EXAMPLE: day 3 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/43)
    - [ ] [EXAMPLE: day 4 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/49)
    - [ ] [EXAMPLE: day 5 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/51)
    - [ ] [EXAMPLE: summary and thank you](https://github.com/coderefinery/2022-03-22-workshop/issues/56)
    - [ ] [EXAMPLE: invitation to debriefing (feedback)](https://github.com/coderefinery/2022-03-22-workshop/issues/52)
- **After the workshop**
  - [ ] Help other roles in putting everybody who contributed and consents on the [website as credit](https://github.com/coderefinery/coderefinery.org/blob/main/content/about/contributors.md)
  - [ ] After the workshop remove the [exercise repositories](https://coderefinery.github.io/git-collaborative/guide/#preparing-exercises)
  - [ ] Help event director with Post-Workshop survey
:::

#### Outreach and marketing coordinator
([description](https://coderefinery.github.io/manuals/workshop-marketing/))
- lead: 
- backup:

:::spoiler Checklist
  - [ ] Coordinate and make sure advertising is happening 
    - [ ] Help instructor coordinator and exercise & team leader coordinator with their outreach
    - [ ] Focus first on getting Local Organisations aboard
  - [ ] Draft email templates
    - [ ] Registration confirmation email
    - [ ] Info to instructors (with instructor coordinator)
    - [ ] Info to observers (with instructor coordinator)
    - [ ] Info to helpers (with exercise coordinator)
    - [ ] Info to team leads (with exercise coordinator)
    - [ ] Info to participants (with registration coordinator)
  - [ ] Create/update [advertising texts](https://github.com/coderefinery/template-workshop-webpage/tree/main/content/communication) and relevant news on the workshop page
  - [ ] After each workshop day, send summary and preparation for next day email to
    all (can be based on the website news and link there so that it can be
    updated)
    - [ ] [EXAMPLE: day 1 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/33)
    - [ ] [EXAMPLE: day 2 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/41)
    - [ ] [EXAMPLE: day 3 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/43)
    - [ ] [EXAMPLE: day 4 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/49)
    - [ ] [EXAMPLE: day 5 summary](https://github.com/coderefinery/2022-03-22-workshop/issues/51)
    - [ ] [EXAMPLE: summary and thank you](https://github.com/coderefinery/2022-03-22-workshop/issues/56)
    - [ ] [EXAMPLE: invitation to debriefing (feedback)](https://github.com/coderefinery/2022-03-22-workshop/issues/52)
  - After the workshop
    - [ ] Help other roles in putting everybody who contributed and consents on the [website as credit](https://github.com/coderefinery/coderefinery.org/blob/main/content/about/contributors.md)
    - [ ] Help event director with Post-Workshop survey

:::

##### Advertisement channels (outreach lead finds people to do take care of the different channels)

- [ ] Newsletter
  - https://tinyletter.com/coderefinery/archive
  - draft: https://hackmd.io/@coderefinery/CRnewsletter_1_2023
- [ ] Advertising texts on the workshop page
  - https://coderefinery.github.io/2023-03-21-workshop/communication/
  - https://github.com/coderefinery/2023-03-21-workshop/tree/main/content/communication
- [ ] CodeRefinery Twitter
  - https://coderefinery.zulipchat.com/#narrow/stream/119815-general/topic/tweet-toot-suggestions
- [ ] CodeRefinery Mastodon
  - https://coderefinery.zulipchat.com/#narrow/stream/119815-general/topic/tweet-toot-suggestions
- [ ] CodeRefinery LinkedIn
  - https://www.linkedin.com/events/coderefineryworkshopmarch21-23a7031623728480272384/comments/
- [ ] CHCAA LinkedIn (Aarhus University)
- [ ] Partner Twitter, retweet and own tweets
  - [ ] Aalto Scientific Computing
- [ ] Partner newsletters
  - [ ] Sigma2
  - [ ] SNIC/NAISS
  - [ ] ENCCS
  - [ ] CSC
- [ ] Partner websites training calendars
  - [ ] CSC
  - [ ] ENCCS
  - [ ] UiB
  - [ ] AU (Aarhus University)
- [ ] Partner and other email lists
  - [ ] Aalto STEM students
  - [ ] Aalto triton users
  - [ ] Delta doctoral network
  - [ ] UiB researcher
  - [ ] UiB HPC
  - [ ] NERSC Bergen
  - [ ] Bjerknes Bergen
  - [ ] University of Oslo computational biology
  - [ ] University of Oslo Phd and Postdocs
  - [ ] University of Oslo Dcince contact (?)
  - [ ] Research institutes in all countries
- [ ] Partner posters
  - [ ] Aalto (CS,U,NBE,PHYS,VAARE)


### Certificate coordinator

https://coderefinery.github.io/2023-03-21-workshop/certificates/
- lead: 
- backup: ASC team (the process can be run by anyone and we are now using a ticketing system to track requests)

:::spoiler Checklist
- [ ] Make sure that instructions on certificates are disseminated multiple times
  - [ ] Workshop page, emails
	```
	- Learner sends materials to scip _at_ aalto.fi. This opens a ticket in Aalto "esupport" system
	- The person who generates the certificate verifies quickly that the tasks were completed.
	- We then work with https://github.com/coderefinery/generate-certificates to generate PDF certificates
	- Certificate is sent to the person and ticket is closed
	- Aalto specific:
	    - The local version of that repository is at /scratch/rse/generate-certificates/. The commands were slightly modified so that the default working directory is not the home folder
	    - Aalto students can also obtain directly the 1 ECTS credit. See internal process at ASC pages.
	```
:::


## Teacher's planning area


## Schedule Day 1
- 08:50 - 09:00 (10 min) Soft start and icebreaker question
- 09:00 - 09:15 (15 min) Welcome and practical information (Richard?)
- Introduction to version control (part 1/2)
    - 09:15 - 09:30 (15 min) [Motivation - teaching & demo](https://coderefinery.github.io/git-intro/motivation/#motivation)
    - 09:30 - 09:45 (15 min) [Basics - teaching & type along](https://coderefinery.github.io/git-intro/basics/#basics)
    - 09:45 - 10:05 (20 min) [Basics - exercises](https://coderefinery.github.io/git-intro/basics/#exercise-record-changes)
      1. [Record changes](https://coderefinery.github.io/git-intro/basics/#exercise-record-changes)
      2. [Optional: Comparing, renaming, and removing](https://coderefinery.github.io/git-intro/basics/#optional-exercises-comparing-renaming-and-removing) - if time allows
    - 10:05 - 10:15 (10 min) :coffee: :walking: :tea: Break
    - 10:15 - 10:35 (20 min) [Basics - History, commit log, ignoring - teaching](https://coderefinery.github.io/git-intro/basics/#git-history-and-log)
    - 10:35 - 10:50 (15 min) [Branching and merging - teaching](https://coderefinery.github.io/git-intro/branches/#branching-and-merging)
    - 10:50 - 11:10 (20 min) [Branching and merging - exercises](https://coderefinery.github.io/git-intro/branches/#exercise-create-and-commit-to-branches)
        1. [Create and commit to branches](https://coderefinery.github.io/git-intro/branches/#exercise-create-and-commit-to-branches) Teaching resumed before merging branches.
        2. [Optional exercises with branches: Fast-forward merge and Rebasing](https://coderefinery.github.io/git-intro/branches/#optional-exercises-with-branches) - if time allows
    - 11:10 - 11:20 (10 min) :coffee: :walking: :tea: Break
    - 11:20 - 11:35 (15 min) Summarize branching and merging
    - 11:35 - 11:45 (10 min) [Conflict resolution (teaching)](https://coderefinery.github.io/git-intro/conflicts/)
    - 11:45 - 12:05 (20 min) [Exercise conflict resolution](https://coderefinery.github.io/git-intro/conflicts/#exercise-create-and-resolve-a-conflict)
- 12:05 - 12:10 (5 min) :coffee: :walking: :tea: Break
- 12:10 - 12:25 (15 min) Buffer, Q&A session
- 12:25 - 12:30 ( 5 min) Feedback & What will we be doing tomorrow?

## Schedule Day 2
* 08:50 - 09:00 (10 min) Soft start and icebreaker question
* 09:00 - 09:10 (10 min) Recap and Q&A from day 1
* 09:10 - 12:30 [Introduction to version control (part 2/2)](https://coderefinery.github.io/git-intro/)
    - 09:10 - 09:20 (10 min) [Sharing repositories online - teaching/type-along](https://coderefinery.github.io/git-intro/remotes/#sharing-repositories-online) 
    - 09:20 - 09:40 (20 min) Diana Exercise: [Pushing our guacamole recipe repository to GitHub](https://coderefinery.github.io/git-intro/remotes/#pushing-our-guacamole-recipe-repository-to-github)
    - 09:40 - 09:55 (15 min) [Inspecting history - teaching/type-along](https://coderefinery.github.io/git-intro/archaeology/#inspecting-history) 
    - 09:55 - 10:10 :coffee: :walking: :tea: Break
    - 10:10 - 10:40 (30 min) [Inspecting history - breakout room exercises](https://coderefinery.github.io/git-intro/archaeology/#exercise-basic-archaeology-commands) 
        1. [Basic archeology commands](https://coderefinery.github.io/git-intro/archaeology/#exercise-basic-archaeology-commands)
        2. [Optional: Git bisect](https://coderefinery.github.io/git-intro/archaeology/#optional-exercise-git-bisect) - to be done if time allows
    - 10:40 - 10:50 (10 min) Summarize inspecting history
    - 10:50 - 11:05 (15 min) [Undoing and recovering - teaching/type-along](https://coderefinery.github.io/git-intro/recovering/#undoing-and-recovering) 
    - 11:05 - 11:15 :coffee: :walking: :tea: Break
    - 11:15 - 11:35 (20 min) [Undoing and recovering - exercises](https://coderefinery.github.io/git-intro/recovering/#exercise-revert-a-commit) 
        1. [Revert a commit](https://coderefinery.github.io/git-intro/recovering/#exercise-revert-a-commit)
        2. [Modify a previous commit](https://coderefinery.github.io/git-intro/recovering/#exercise-modify-a-previous-commit)
        3. [Git reset](https://coderefinery.github.io/git-intro/recovering/#exercise-git-reset)
    - 11:35 - 11:50 (15 min) Summarize undoing and recovering and discussion and mention that staging area exists
    - 11:50 - 12:00 :coffee: :walking: :tea: Break
    - 12:00 - 12:25 (25 min) [How much Git is necessary?](https://coderefinery.github.io/git-intro/level/#practical-advice-how-much-git-is-necessary) 
    - 12:25 - 12:30 (05 min) Feedback & What will we be doing tomorrow?

## Schedule Day 3

* 08:50 - 09:00 Soft start and icebreaker question
* 09:00 - 09:15 Recap Git, any Hackmd questions to highlight
  - 09:15 - 09:30 Concepts around collaboration
    1. Explain terms. Pull, push, clone, fork. Focus on pull and not fetch.
    2. Focus more on Clone and less on Generating from templates and importing
  - 09:30 - 11:10 Centralized workflow + a break
    - 9:30 - 9:45 : Explain concepts.
    - 9:45 - 9:55 break
    - 9:55 - 10:00 Inform clearly what is expected outcome.
    - 10:00 - 10:30 Exercise
    - 10:30 - 10:50 Instructors go through the exercise
    - 10:50 - 11:00 - break
  - 11:00 - 12:10 Distributed version control and forking workflow + one breake
    - 11:00 - 11:15 - Concepts and what are exercise outcomes
    - 11:15 - 11:45 - Exercise
    - 11:45 - 12:00 - Instructors go through excercises
    - 12:00 - 12:10 - break
  - 12:10 - 12:30 - How to contribute changes to somebody else’s project and Q&A


## Schedule Day 4

* 08:50 - 09:00 Soft start and icebreaker question
* 09:00 - 09:10 Interview with an expert
* 09:10 - 11:15 [Reproducible research](https://coderefinery.github.io/reproducible-research/)
    - 09:10 - 09:20 [Motivation](https://coderefinery.github.io/reproducible-research/motivation/)
    - 09:20 - 09:30 [Organizing your projects](https://coderefinery.github.io/reproducible-research/organizing-projects/)
    - 09:30 - 10:00 [Recording dependencies](https://coderefinery.github.io/reproducible-research/dependencies/)
       - discussion (5 min)
       - [exercise (20 min)](https://coderefinery.github.io/documentation/writing-readme-files/#exercises)
       - discussion (5 min)
    - 10:00 - 10:10 Break
    - 10:10 - 10:40 [Recording computational steps](https://coderefinery.github.io/reproducible-research/workflow-management/)
       - discussion (5 min)
       - [exercise (20 min)](https://coderefinery.github.io/reproducible-research/workflow-management/#exercise-using-snakemake)
       - discussion (5 min)
    - 10:40 - 10:50 [Recording environments](https://coderefinery.github.io/reproducible-research/environments/)
    - 10:50 - 11:05 [Sharing code and data](https://coderefinery.github.io/reproducible-research/sharing/)
        - [demo (15 min)](https://coderefinery.github.io/reproducible-research/sharing/#connecting-repositories-to-zenodo)
    - 11:05 - 11:15 Break
* 11:15 - 12:30 [Social coding](https://coderefinery.github.io/social-coding/)
  - 11:15 - 11:30 [Social coding (15 min)](https://coderefinery.github.io/social-coding/social-coding/)
  - 11:30 - 12:00 [Licensing (30 min)](https://coderefinery.github.io/social-coding/licensing/)
  - 12:00 - 12:15 [Software citation (15 min)](https://coderefinery.github.io/social-coding/software-citation/)
  - 12:15 - 12:25 (10 min) Buffer, Q&A session
  - 12:25 - 12:30 (5 min) Feedback & What will we be doing tomorrow?

## Schedule Day 5

* 09:00 - 10:45 [Jupyter](https://coderefinery.github.io/jupyter/)
    - 09:00 - 09:10 [Jupyter notebooks](https://coderefinery.github.io/jupyter/motivation/)
    - 09:10 - 09:25 [JupyterLab and notebook interface](https://coderefinery.github.io/jupyter/interface/)
    - 09:25 - 09:50 [A first computational notebook](https://coderefinery.github.io/jupyter/first-notebook/)
      - intro to the exercise (5 min)
      - [breakout room exercise (20 min)](https://coderefinery.github.io/jupyter/sharing/)
    - 09:50 - 10:00 [Notebooks and version control demo, 10-15 min](https://coderefinery.github.io/jupyter/version-control/)
    - 10:00 - 10:10 Break
    - 10:10 - 10:35 [Sharing notebooks](https://coderefinery.github.io/jupyter/sharing/)
      - [Binder Breakout room exercise (20 min)](https://coderefinery.github.io/jupyter/sharing/#sharing-dynamic-notebooks-on-binder)
    - 10:35 - 10:40 Wrap-up
    - 10:40 - 10:45 buffer

* 10:45 - 12:30 [Documentation](https://coderefinery.github.io/documentation/)
    - 10:45 - 10:55 [Motivation and tools](https://coderefinery.github.io/documentation/wishlist/)
        - create a wishlist in HackMD
    - 10:55 - 11:05 Break
    - 11:00 - 11:20 [Writing good README files](https://coderefinery.github.io/documentation/writing-readme-files/#writing-good-readme-files)
        - brief discussion
        - [15 minutes for exercises](https://coderefinery.github.io/documentation/writing-readme-files/#exercises), choosing either 1, 2 or 3 (or do multiple of time allows)
        - brief discussion
    - 11:20 - 12:00 [Sphinx and markdown](https://coderefinery.github.io/documentation/sphinx/)
        - discussion (5 min)
        - [Exercise 1 as type along (10 min)](https://coderefinery.github.io/documentation/sphinx/#exercise-sphinx-basics)
        - [Exercise 2, exercise 3 if time allows (20 min)](https://coderefinery.github.io/documentation/sphinx/#exercise-sphinx-content)
        - Discussion, going over exercise (5 min)
    - 12:00 - 12:10 Break
    - 12:10 - 12:25 [Deploying Sphinx documentation to GitHub Pages](https://coderefinery.github.io/documentation/gh_workflow/#deploying-sphinx-documentation-to-github-pages)
        - [Exercise 1 as demo](https://coderefinery.github.io/documentation/gh_workflow/#exercise-deploy-sphinx-documentation-to-github-pages)
    - 12:25 - 12:30 [Summary](https://coderefinery.github.io/documentation/summary/)

## Schedule Day 6

**Day 6**
* 8:50 - 9:00 Getting started
* 9:00 - 10:45 [Software testing](https://coderefinery.github.io/testing/)
  - 9:00-9:05 Short info about today's exercise sessions and possible questions from yesterday
  - 9:05-9:10 [Motivation](https://coderefinery.github.io/testing/motivation/)
  - 9:10-9:20 [Concepts](https://coderefinery.github.io/testing/concepts/)
  - 9:20-9:45 [Testing locally](https://coderefinery.github.io/testing/pytest/)
      - 5 minutes talking
      - 15 minute exercises
      - 5 going over exercises and discussion
  - 9:45-9:55 Break
  - 9:55-10:20 [Automated testing](https://coderefinery.github.io/testing/continuous-integration/)
      - type-along session
  - 10:20-10:45 [Test design](https://coderefinery.github.io/testing/test-design/)
      - discussion: 5 minutes
      - Exercises: 10 minutes.  Any of exercises Design-1 to Design-8 that learners want to do.
      - discussion and type-along of advanced exercises: 10 minutes
  - 10:45-11:00 Break
* 11:00 - 12:15 [Modular coding](https://coderefinery.github.io/modular-type-along/)
* 12:15 - 12:30 [Concluding remarks and where to go from here](https://github.com/coderefinery/workshop-outro/blob/master/README.md)

- and more: https://coderefinery.github.io/2023-03-21-workshop/join/#accessibility


## Lessons learned / new ideas
- Add ideas here as they come and combine in a blog post after the workshop
