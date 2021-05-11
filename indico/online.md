# Indico online workshop workflow

This describes the workflow in Indico online workshops

## Basic types

Registration types = {Learner, Exercise Leader, Livestream only}

## Flow

* People may register in any of the types.
* When people get accepted to `Type={Learner,Exercise Leader}`, they are
  confirmed using the Indico moderation "approve registrations"
  feature. (These people then become `State=Completed`)
* After soft deadline, accept the number of learners you think you can
  handle (see above).
  * Non-accepted people are moved to `Type=Livestream` but this is
    mainly to help them, people can still register.
* A new field "I confirm I can attend via Zoom" is made visible.
  Everyone in  `State=Completed` is expected to log in and click this
  box.
  * Other non-accepted people
* Those who do not make `Confirm=Yes` are moved to `Type=Livestream`.
  * Note: any saving of the form, even by staff, will set
    `Confirm=No`.  So `Confirm=No` does *not* mean that they declined,
    it could also be staff who saved the form.
* If there are remaining free spots, they are given to those who are
  `Type=Livestream Confirm=Yes`.
* Everyone else is set to `Type=Livestream`
* The event registration form is edited, so that the number of
  `Type=Learner` spots is set to the actual number registered.  Then,
  no one else can register as a learner.
  * This could be done a bit earlier in the process, but it prevents
    even organizers from moving people between categories. Thus, it's
    slightly more convenient to leave it free than have to adjust the
    registration form every time you need to switch someone to learner
    (for example, registering on a team)

## Email filters

During registration

* People who want to in Zoom, `State!=Withdrawn Type={Learner,Exercise
  Leader}`

After confirmation

* People in Zoom, `State!=Withdrawn Type={Learner,Exercise Leader}`
* PEople in livestream, `State!=Withdrawn Type=Livestream`




