# Indico event setup

We use the NeIC Indico service, <https://indico.neic.no/>, so you need to create
an account at <https://indico.neic.no/login/>.

RB is manager of the CodeRefinery category in
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
  "Registration forms". **Do not clone** "ACLs and protection settings".
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
   - Then go back to "Manage" and verify and configure the "Registration Form":
     read all fields and check that nothing outdated has been cloned to this
     event. Adapt the dates.


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
