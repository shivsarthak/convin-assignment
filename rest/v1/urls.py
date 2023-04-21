from django.urls import include, path

urlpatterns = [
    path('calendar/', include('rest.v1.calendar.urls')),
]
