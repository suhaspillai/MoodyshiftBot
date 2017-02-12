# howdy/urls.py
from django.conf.urls import  url
from getemotion import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^list/$', list, name='list')
]