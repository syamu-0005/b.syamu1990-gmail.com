"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
# from firstApp import views
from testApp import views
from greetingApp.views import greetings_view
from timeApp.views import time_info_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^greeting/', views.display_view),
    url(r'^morning/', views.good_morning_view),
    url(r'^afternoon/', views.good_afternoon_view),
    url(r'^evening/', views.good_evening_view),
    url(r'^night/', views.good_night_view),
    url(r'^greetings/', greetings_view),
    url(r'^time/', time_info_view),
]
