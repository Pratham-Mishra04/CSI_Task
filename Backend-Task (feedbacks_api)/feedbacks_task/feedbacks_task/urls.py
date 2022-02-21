"""feedbacks_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name="Landing Page"),
    path('api/',views.apiOverview,name="Api Overview"),
    path('api/feed-detail/',views.feedList, name="Feed List"),
    path('api/feed-detail/<str:pk>/',views.feedDetail, name="Feed Detail"),
    path('api/feed-create/',views.feedCreate, name="Feed Create"),
    path('api/feed-update/<str:pk>/',views.feedUpdate, name="Feed Update"),
    path('api/feed-delete/<str:pk>/',views.feedDelete, name="Feed Delete"),
]
