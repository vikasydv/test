from django.urls import path

from ch4.views import Homepageview
urlpatterns = [
    path('',Homepageview.as_view(),name='home')
]
