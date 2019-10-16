

# Select a workhop coordinator

One or two persons coordinate the workshop preparation and debrief. This does
not mean that they do all the work - they are encouraged to delegate tasks -
but they make sure that nothing gets forgotten.


# Other documents and references

- Workshop organization overview: https://github.com/orgs/coderefinery/projects/4
- Instructions on how to set up a registration page: [indico-workshop-management.md](indico-workshop-management.md)
- Email templates for workshop communication (to be migrated this repo): [CR Google drive/manuals/email-templates/](https://drive.google.com/drive/folders/0B3i0ZRReqpSxTXpGUVVTbmtuX0k)


# Pre-workshop

First steps:
- Assemble a team of 3 instructors
- Reserve dates (coordinate this with the instructors)
- Reserve room
- Select a workshop coordinator
- Workshop coordinator creates a ticket with a checklist on https://github.com/orgs/coderefinery/projects/4 and takes it (self-assigns)

Set up workshop page:
- Import the template at https://github.com/coderefinery/template-workshop-webpage to your username
  or the coderefinery organization, and name it like "2019-10-16-somecity".
- Update the required fields in `index.md` and push the commits. 
  The page should now be served at *username.github.io/2019-10-16-somecity/*.
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

Announcing the workshop:
- Twitter
- Email persons who registered to notify-me form
- Use local mailing lists and all channels possible

Distribute the work:
- Make sure lessons are distributed
- Recruit helpers

Prepare practicals:
- Order catering (coffee, tea, water, fruit, something sweet, etc.)
- Organize sticky notes
- Organize extension cables if needed
- Organize alternative wireless for those without Eduroam (if any)

Keep communication with participants:
- Remind registered participants that they are either expected to show up or to cancel participation
- Maintain waiting list if needed
- Make sure we have enough pre-survey answers
- Close registration on the workshop page

1-2 weeks before the workshop:
- Workshop coordinator organizes a call with all instructors and helpers to discuss the schedule to leave no doubts about timing. Also
  discuss the survey results.
- Send out practical information, including installation instructions, 2-3 week ahead. Also ask those without Eduroam to speak up.
  [Here is a template](templates/practical-info-to-participants.txt)

Right before the workshop starts:
- Prepare a shared Google doc with global write permissions, consider creating a memorable short-link


# Create exercise repositories

- The collaborative Git lesson requires exercise repositories to
  be set up. For this follow the instructor guide in the lesson material.


# As participants arrive

- Emphasize to participants that you need to sit with someone - don't work alone.
- Try to have participants sit next to someone with a similar operating
  system if they have no preference, since they will face similar
  problems.


# Introduction talk

- See https://github.com/coderefinery/workshop-intro


# During workshop

- Keep up interactive feel by encouraging and asking questions
- Keep time
- For presentations which have shell commands, create a
  cheatsheet/reference on the board in real time.
- Remind participants about sticky notes.
- Make sure we take regular breaks (at least a short break each hour)
- Give participants some time to also experiment (do not rush the classroom through exercises)
- Encourage optional feedback at the end of each day on sticky notes
- Create GitHub issues for points which are confusing or problematic
- Take active part even in the lessons you're not teaching, e.g. by asking
  questions and (politely) interject with clarifications when you think
  something is confusing to the learners


# At the end of workshop

- Give credit to those who contributed and helped
- Use https://github.com/coderefinery/workshop-outro


# Post-workshop

- Process and distribute feedback
- Debrief with instructors
- Process certificate requests
