# Indico event setup

We use the NeIC Indico service, <https://indico.neic.no/>, so you need to create
an account at <https://indico.neic.no/login/>.

Radovan is manager of the CodeRefinery category in
indico.neic.no and will need to grant you permissions to create event pages.

To create a new workshop page, it is easiest to clone a previous event. This
copies the registration form and metadata, but not the pre-workshop survey
which needs to be manually imported as a json file.


## Step-by-step instructions:

### Copy basics from latest event

- Visit <https://indico.neic.no/>, and click CodeRefinery which takes you to <https://indico.neic.no/category/5/>.
- Click the latest workshop event. You might need to show "events in the future" to see the latest event.
- Go to admin mode (click the pen symbol on top toolbar, "Switch to the management area of this event").
- Click the "Clone" button, and select "Clone Once". Click "Next" button.
- For "What should be cloned", select
  "Registration forms" (do not clone "ACLs and protection settings").
  Uncheck "Refresh user information". Click "Next".
- Confirm category "CodeRefinery", and click "Next".
- Select the start date and time of the workshop, click "Clone".
- You are now on the cloned event page (confirm that the event number changed), and you should start updating the information.

### Update copied event information

- Adjust permissions so that only the workshop organizer(s)/coordinator(s) has/have access to the forms and data.
  In order to have better control over who has access we do not copy "ACLs and protection settings" from older events.
- Update the Title, Description, Date, Time, Room, Venue and Address fields by clicking the pen symbols on the right.
- Click "Protection" and remove administrators who were copied from past event but should not have access to this event.
- Click "Registration" from the left-hand menu, and confirm that there is one or two registration forms, probably with a wrong title.
- Click the "Manage" button on the "List of registration forms",
   - Click "Edit" on the "General settings"
   - Update the registration form name and both the fields "Contact info" and "List of recipients" with your own email address to get notifications on new registrations.
   - **Waiting list:**
   - *Indico doesn't have an actual waiting list functionality. To implement a waiting list, we use moderated registrations and confirm all registrations up to max capacity (eg. 40). Registrations after that up to maximum number of participants (eg. 60) are left unconfirmed and an email is sent manually from Indico to the registrant that they are on the waiting list. Now we have a waiting list of size 60 - 40 = 20.*
   - Activate "Moderated" which will require each registration to be approved.
   - Set maximum number of participants (after which registration is closed), this should be *room capacity* + *waiting list size*. Click "Save".
   - Then go back to "Manage" and verify and configure the "Registration Form":
     read all fields and check that nothing outdated has been cloned to this
     event. Adapt the dates.

#### More information about the registration process

- The Description field in the general settings should contain additional information about the registration process:
   ```
   Welcome to the registration page for the Online CodeRefinery workshop March 22-24 and 29-31!

   To complete your registration, you need to:

   1) Enter your registration details by clicking the "Register now" button below.
   2) Fill in the pre-workshop survey by clicking the "Fill out the survey" button below.

   Confirmation email
   After filling out the registration form you will receive an automatic
   confirmation email, but please note that all registrations go to a waiting
   list first. Please contact to support@coderefinery.org if you don't receive
   this confirmation email within a couple of days after signing-up. 

   Questions?
   If you have any questions about your registration status, please write to support@coderefinery.org.

   Looking forward to seeing you at the workshop!
   ```

### Import survey

- Now click "Surveys" from the left hand menu. You will now import the standard pre-workshop survey from a json file.
- Go to <https://github.com/coderefinery/pre-workshop-survey> and clone the repository.
- Go back to the Indico Surveys page, and click "Create survey"
- Name the survey "Pre-workshop survey", enable the option "Anonymous submissions" and disable "Only logged-in users". Click "Save".
- Back on the "Surveys" page, click "Manage" on the newly created "Pre-workshop-survey" survey.
- It will say "Survey not ready". Click "Prepare questionnaire".
- Click the "Import" button, click "Choose from your computer", and find the file exported-survey.json" from the pre-workshop-survey repository you cloned. Click "Save".
- Go back to the survey page (click "Surveys" on the left), and click "Manage". Click the "Open now" button to let the survey go live.


### Open registration

- Go to the Registration page from the left-hand menu, and click "Manage".
- It will say "Registrations are not open yet". Click "Start now" for both regular and staff registration forms to open for registrations.
- Click the blue "Switch to display view" on the top left.
- Confirm that both the "Surveys" and "Registration" links can be seen.
- Click both links to do a test registration
- Once you manage to test-register, update the workshop webpage, and announce via Twitter.


### Exporting registrations

- Go to the Registration page from the left-hand menu, and click "Registrations" which 
  takes you to the list of registrations..
- Click the check-box on the menu just above the list of registrations and select "All".
- Click on "Export" from the top menu, select "CSV" and choose a download directory.
- You can use the [read_csv.py](https://github.com/coderefinery/manuals/blob/master/scripts/read_csv.py) to parse the CSV file and print 
  selected fields, e.g. email addresses to be used in sending out information to 
  participants.
