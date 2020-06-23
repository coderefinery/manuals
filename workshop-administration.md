
# Organizing a CodeRefinery workshop

Anyone can organize a CodeRefinery workshop and teach the CodeRefinery lessons which are
licensed under [CC-BY](https://creativecommons.org/licenses/by/4.0/).
However, making it a successful workshop requires careful planning and preparation. Here we will go
through practical aspects of organizing a workshop.

## Select a workshop coordinator

One or two persons coordinate the workshop preparation and debrief. This does
not mean that they do all the work - they are encouraged to delegate tasks -
but they make sure that nothing gets forgotten.


## Other documents and references

- Workshop organization overview: https://github.com/orgs/coderefinery/projects/4
- Instructions on how to set up a registration page in Indico (for NeIC affiliated staff):
  [indico-workshop-management.md](indico-workshop-management.md)
- Email templates for workshop communication:
  - [1-2 weeks before workshop starts](templates/practical-info-to-participants.txt)
  - [advertising workshop via private communication](templates/advertising-workshop.txt)

## Before the workshop

#### First steps

- Recruit instructors - having at least 3 instructors is highly recommended.
- Find 1-2 workshop helpers [with an appropriate background](workshop-requirements.md).
- Reserve dates (coordinate this with the instructors)
- Reserve room
- Select a workshop coordinator
- Workshop coordinator creates a ticket with a checklist on https://github.com/orgs/coderefinery/projects/4 and takes it (self-assigns)

#### Lecture room

- Start looking for an appropriate lecture room early.
- See this [list of requirements](workshop-requirements.md) for
  the lecture room.

#### Set up workshop page

- Import the template at https://github.com/coderefinery/template-workshop-webpage to your username
  or the coderefinery organization, and name it like "2019-10-16-somecity".
- Update the required fields in `index.md` and push the commits.
  The page should now be served at *username.github.io/2019-10-16-somecity/*.
- If the workshop will be customized to the needs of a particular audience, modify the schedule accordingly.
- If the workshop should be listed on https://coderefinery.org:
  - (Fork and) clone https://github.com/coderefinery/coderefinery.org
  - Under `coderefinery.org/_workshops/`, add a file named like `2019-10-16-somecity.md` which contains
    the fields permalink, city and dates. For example:
    ```
    ---
    permalink: https://username.github.io/2019-10-16-city/
    city: Somecity
    dates: October 16-18, 2019
    ---
    ```
  - send a pull request with your new file.
- Create a registration form following [indico-workshop-management.md](indico-workshop-management.md).
- Open and test registration

#### Announcing the workshop

- Twitter
- Email persons who registered to notify-me form
- Use local mailing lists and all channels possible

For self-organized workshops:
- Write an email to support@coderefinery.org to get a pre-workshop survey link and registration form on
  [https://indico.neic.no](https://indico.neic.no)


#### Distribute the work

- Make sure lessons are distributed

#### Prepare practicals

- Order catering (coffee, tea, water, fruit, something sweet, etc.)
- Organize sticky notes
- Organize extension cables if needed
- Organize alternative wireless for those without Eduroam (if any)

#### Communication with participants

- Send out practical information, including installation instructions, around 2 weeks ahead.
  [Here is a template](https://github.com/coderefinery/manuals/blob/master/templates/practical-info-to-participants.txt).
- Emphasize that all software should be installed before the workshop starts, and point out
  the [configuration problems and solutions](https://coderefinery.github.io/installation/troubleshooting/).
- Remind registered participants that they are either expected to show up or to cancel participation
- Also ask those without Eduroam to speak up.
- Maintain waiting list if needed
- Make sure we have enough pre-survey answers
- Close registration on the workshop page

#### 1-2 weeks before the workshop

- Workshop coordinator organizes a call with all instructors and helpers to discuss the schedule to leave no doubts about timing. Also
  discuss the survey results.
- Point helpers (and instructors) to the [tips for helpers](helping-and-teaching.md).

#### Right before the workshop starts

- Prepare a shared Google doc or https://hackmd.io with global write permissions,
  consider creating a memorable short-link (e.g. bit.ly)


## Create exercise repositories

- The collaborative Git lesson requires exercise repositories to
  be set up. For this follow the instructor guide in the lesson material.


## As participants arrive

- Emphasize to participants that you need to sit with someone - don't work alone.
- Try to have participants sit next to someone with a similar operating
  system if they have no preference, since they will face similar
  problems.


## Introduction talk

- See https://github.com/coderefinery/workshop-intro


## During workshop

- Keep up interactive feel by encouraging and asking questions
- Keep time
- For presentations which have shell commands, create a
  cheatsheet/reference on the board in real time.
- Remind participants about sticky notes.
- Make sure we take regular breaks (at least a short break each hour)
- Give participants some time to also experiment (do not rush the classroom through exercises)
- Encourage optional feedback at the end of each day or end of each lesson
  on sticky notes. Process the feedback immediately and adjust your teaching
  (pace etc) accordingly
- Create GitHub issues for points which are confusing or problematic
- Take active part even in the lessons you're not teaching, e.g. by asking
  questions and (politely) interject with clarifications when you think
  something is confusing to the learners


## At the end of workshop

- Give credit to those who contributed and helped
- Use https://github.com/coderefinery/workshop-outro


## Post-workshop

- Process and distribute feedback
- Debrief with instructors
- Process certificate requests
