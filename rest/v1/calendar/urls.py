from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.GoogleCalendarInitView, name='google_calendar_init'),
    path('redirect/', views.GoogleCalendarRedirectView,
         name='google_calendar_redirect'),
]
