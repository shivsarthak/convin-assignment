# Convin Assignment: Google Calendar Integration using Django REST API


This project is a solution to the Convin Assignment, where the task was to implement Google Calendar integration using Django REST API. The project uses OAuth2 mechanism to get user's calendar access and fetches a list of events from the user's calendar.

## Requirements
---
The project requires the following to be installed:

- Python 3.9 or above
- Django 3.2 or above
- google-auth library
- google-auth-oauthlib library
- google-auth-httplib2 library
- google-api-python-client library
- python-dotenv

## Installation
------------
To run the project on your local machine, follow the steps below:

1. Clone the repository using `git clone https://github.com/shivsarthak/convin-assignment.git`

2. Install the dependencies using `pip install -r requirements.txt`

3. Create a `.env` file in the project directory and add the following:

    ```
    CLIENT_ID=<your_google_oauth2_client_id>
    CLIENT_SECRET=<your_google_oauth2_client_secret>
    REDIRECT_URI=http://localhost:8000/rest/v1/calendar/redirect/
    ```

    Make sure to replace the placeholders with your own Google OAuth2 client ID and secret.

4. Run the Django server using `python manage.py runserver`

5. Navigate to `http://localhost:8000` in your browser to access the home page.

6. Click on the "Go to Endpoint" button for /rest/v1/calendar/init to initiate the OAuth flow.

## API Endpoints
-------------
The project has two API endpoints:

- `/rest/v1/calendar/init/` - This endpoint starts step 1 of the OAuth flow and prompts the user for their credentials.
- `/rest/v1/calendar/redirect/` - This endpoint handles the redirect request sent by Google with the access token and fetches a list of events from the user's calendar.

## Project Structure
------------------
The project has the following structure:
```
convin/
│   .env
│   .gitignore
│   manage.py
│   readme.md
│   requirements.txt
│
├───rest
│   │   asgi.py
│   │   db.sqlite3
│   │   settings.py
│   │   urls.py
│   │   views.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───v1
│       │   urls.py
│       │   __init__.py
│       │
│       └───calendar
│               credentials.json
│               google.py
│               urls.py
│               views.py
│               __init__.py
│
└───templates
        home.html
```

- `rest/` contains the Django project settings.
- `rest/v1/calendar` contains the views mentioned in the task
- `templates/` contains the HTML template for the home page.
- `.env` contains the environment variables.
- `manage.py` is the command-line utility to manage the Django project.
- `requirements.txt` contains the list of dependencies required for the project.
