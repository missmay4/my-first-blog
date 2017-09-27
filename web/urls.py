from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main_web),
    url(r'^about_me$', views.aboutme)


    ]
