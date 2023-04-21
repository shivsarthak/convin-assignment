from django.urls import path, include
from .views import home
urlpatterns = [
    path('rest/v1/', include('rest.v1.urls')),
    path('', home, name='home'),
]
