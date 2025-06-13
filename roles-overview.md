(roles)=

# Roles overview

CodeRefinery has been able to scale online workshops while maintaining
an interactive feeling. This page describes the roles that we use in our workshops.

Despite the many different roles documented here, **in practice many
of them are occupied by the same people**.
{ref}`Best-practices` below tells more about what tends to happen.
One of the advantages of our large workshops is that we have many more
staff on hand (often 10-15), thus allowing much more specialization
than small workshop can have (thus, the large number of roles below).
Many of our instructors give feedback such as "this is so much easier:
we only show up and teach!"

A common pathway goes (Learner/team leader) → (Expert
helper/Instructor) → (More specialized roles).  **Note that thanks to
our {doc}`team teaching or "co-teaching" <team-teaching>`, it is really easy to join as
an instructor!**

You can also find the common tasks in checklist-format under each roles section in the {doc}`Workshop playbook <workshop-playbook>`.

## Workshop roles

### Learner

Comes and learns.

* Does necessary preparation and attends the workshop
* More info: {ref}`Learners section <toc-learners>`

### Team leader

Team leaders are only a small step above learners.  They aren't
expected to know everything, but mainly keep their breakout rooms on
track - they could even be a slightly more confident learner.

* Leads a breakout room
  * keeps on track
  * makes welcoming community
  * answers some questions
  * ask for more help when needed
* Attends a one-hour team leader preparation / onboarding session.
* More info: {doc}`team-leaders`

### Instructor

Obviously, instructors teach.  Uniquely in our system, they have a lot
of support and generally can focus on the teaching part.

* Prepares lesson and "just teaches" without worrying about other workshop matters
* {doc}`Team teaching <team-teaching>`, you are not alone
* Attend instructor preparation calls
* Usually receives one-on-one mentoring in advance
* Other times during the workshop, usually serves as an expert helper
* More info: {doc}`instructors`

### Expert helper

Expert helpers are generalists who don't have other assigned roles.

* All-around generalist who assists wherever is needed
* Answers questions in notes document
* Supports team leaders 
* Identifies important issues and raises them to the instructors,
  "voice of the audience"
* More info: {doc}`expert-helpers`

### Behind the scenes

#### Notes manager

The notes manager closely watches notes document to keep it organized and by
reading it in detail, can serve as the "voice of the audience" to the
instructors.

* Ensures everything gets some answer quickly
  * Even if it is "will be answered later"
  * Can raise issues to instructors immediately if needed.
  * In general serves as the instructors' "ear on the ground"
* Maintenance during the workshop
  * Copies old information to archive notes document if too much traffic
  * Organizes sections and questions
  * Notes break and exercise times
* Processes and archives notes after the course.
* More info: {doc}`hackmd-helper`

#### Host

The Host serves as the manager of learners during the course.

* Learner Zoom meeting host (often).  Often the registration
  coordinator.
* Helps learners with organizational issues during the course
  * Ensures that everyone is welcomed and knows what is going on
  * Assign learners to breakout rooms
  * Answers technical questions about the course itself
* Often the same person as the registration coordinator.
* More info: {doc}`host`

#### Director

The director manages the flow of the course: preparing and cueing
instructors, switching the livestream scenes, announcing schedule,
adjusting schedule as needed.

* Instructor Zoom meeting host (often).  Often the instructor
  coordinator.
* Cues the sessions, makes sure they flow together well.
* Adjusts the flow when things do *not* go according to schedule.
* Has sufficient knowledge of the tech setup to do the scene
  switching.
* More info: {doc}`director`


#### Broadcaster (livestream)

The broadcaster is responsible for the livestreaming tech.

* Only needed in livestream courses
* Installs and manages OBS control for livestreams
  * Ideally is not teaching in the first session
  * Is around in case of problems, otherwise the director does most of
    the scene switching.
* Makes sure videos get processed and to Youtube in a timely manner,
  or at least saves them where someone else can do it.
* More info: {doc}`broadcaster`

#### Registration coordinator

Oversees registration and generally everything on the participant side.

* Communicate with participants
* Organize installation help session
* Contact person for learners
* Collect feedback
* Provide participation certificates
* More info: {doc}`registration-coordinator`)

#### Instructor coordinator

* Find instructors
* Coordinate the schedule and instructors for each event
* Organize {doc}`instructor onboarding <instructor-intro>`
* Collect feedback
* More info : {doc}`instructors`.

#### Outreach and marketing coordinator

* Makes sure workshop gets advertised in different places
* You can find a list of commonly advertised places in the bottom of the {doc}`workshop-playbook`.

### Team leader / Exercise coordinator

* Communicate with all team leaders, contact person for them
* Makes sure all exercises are ready and commicated before and during the workshop
* Organize the {doc}`team leader onboarding session <team-leaders>`
* Usually attends as an expert helper to generally be available and
  support all leaders.
* Collect feedback from team leaders
* More info: {doc}`exercise-coordinator`

### Video editor

* Watches videos and prepares for YouTube upload
* Uses
  [ffmpeg-editlist](https://github.com/coderefinery/ffmpeg-editlist)
  to process videos after the Broadcaster has made them available.
* Work should be done the day/evening of of the course

(best-practices)=
## Best practices

Roles that are often combined:

* **Registration coordinator** and **Host**
* **Instructor coordinator** and **Director**
* **Expert helper** and anything
* **Instructor** and any other role (but not **Host**)

Roles that should *not* be combined:

* **Registration coordinator** and **Instructor coordinator** (these
  two together tend to form the "core team")
* **Broadcaster**/**Director** and **Instructor** on the first sessions of each
  day.
* **Notes manager** and other roles (so *delegate* notes editing while you do
  something else!  this is OK.)
* **Host** and any active teaching (in big workshops at least -
  learner management keeps you busy)

Other notes:

* **Notes manager** can rotate between different people on different days.
* **Expert helpers** can replace **team leaders** if they cannot join the
  full workshop
* Coordinators delegate
