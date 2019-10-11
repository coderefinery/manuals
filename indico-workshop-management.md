# Guide on how to use Indico for managing workshops 

We use the NeIC Indico service, https://indico.neic.no/, so you need to create an account at https://indico.neic.no/login/ 

Radovan, Thor, and Sabry are managers of the CodeRefinery category in indico.neic.no and will need to grant you permissions to create event pages.

To create a new workshop page, it is easiest to clone a previous event. This copies the registration form and metadata, but not the pre-workshop survey which needs to be manually imported as a json file.

## Step-by-step instructions:
### Copy basics from latest event
- Visit https://indico.neic.no/, and click CodeRefinery which takes you to https://indico.neic.no/category/5/.
- Click the latest workshop event.
- Go to admin mode (click the pen symbol on top toolbar, “Switch to the management area of this event”).
- Click the “Clone” button, and select “Clone Once”. Click “Next” button.
- For “What should be cloned”, select “ACLs and protection settings” and “Registration forms”. Click “Next”
- Confirm category “CodeRefinery”, and click Next
- Select the start date and time of the workshop, click Next.
- You are now on the cloned event page (confirm that the event number changed), and you should start updating the information. 
### Update copied event information
- Update the Title, Description, Date, Time, Room, Venue and Address fields by clicking the pen symbols on the right.
- Click “Registration” from the left-hand menu, and confirm that there’s a registration form. 
- Click the “Manage” button on the “List of registration forms”,
   - Click “Edit” on the “General settings”
   - Update the registration form name and both the fields “Contact info” and “List of recipients” with your own email address to get notifications on new registrations. 
   - **Waiting list:**
   - *Indico doesn't have an actual waiting list functionality. To implement a waiting list, we use moderated registrations and confirm all registrations up to max capacity (eg. 40). Registrations after that up to maximum number of participants (eg. 60) are left unconfirmed and an email is sent manually from Indico to the registrant that he/she is on the waiting list. Now we have a waiting list of size 60 - 40 = 20.*
   - Activate “Moderated” which will require each registration to be approved.
   - Set maximum number of participants (after which registration is closed), Click “Save”. This should be *room capacity* + *waiting list size*.
### Import survey
- Now click “Surveys” from the left hand menu. You will now import the standard pre-workshop survey from a json file.
- Go to https://github.com/coderefinery/pre-workshop-survey and clone the repository.
- Go back to the Indico Surveys page, and click “Create survey”
- Name the survey “Pre-workshop survey”, enable the option “Anonymous submissions” and disable “Only logged-in users”. Click “Save”.
- Back on the “Surveys” page, click “Manage” on the newly created “Pre-workshop-survey” survey.
- It will say “Survey not ready”. Click “Prepare questionnaire”.
- Click the “Import” button, click “Choose from your computer”, and find the file exported-survey.json” from the pre-workshop-survey repository you cloned. Click “Save”.
- Go back to the survey page (click “Surveys” on the left), and click “Manage”. Click the “Open now” button to let the survey go live.
### Open registration
- Go to the Registration page from the left-hand menu, and click “Manage”.
- It will say “Registrations are not open yet”. Click “Start now” to open for registrations.
- Click the blue “Switch to display view” on the top left.
- Confirm that both the “Surveys” and “Registration” links can be seen. 
- Click both links to do a test registration
- Once you manage to test-register, update the workshop webpage, and announce via Twitter.
