from django.http import JsonResponse
from django.shortcuts import redirect
from googleapiclient.discovery import build

from .google import flow
import datetime


def GoogleCalendarInitView(request):
    # Start the OAuth flow
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    response = redirect(authorization_url)
    return response


def GoogleCalendarRedirectView(request):
    # Get Access token from the authorization server
    try:
        flow.fetch_token(authorization_response=request.build_absolute_uri())
        service = build('calendar', 'v3', credentials=flow.credentials)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
    except:
        # If the auth token is invalid or already used
        # redirect to the the init view
        return redirect('/rest/v1/calendar/init/')
    return JsonResponse({'description': 'Upcoming 10 Google Calendar Events',
                         'events': events}, safe=False)
