from django.urls import path
from . import views

urlpattern = [
    path('api/',views.apiOverview, name="api-overview"),
    path('feed-list/',views.feedlist, name="feed-list"),
]