# howdy/urls.py
from django.conf.urls import url
from getemotion import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]