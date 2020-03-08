from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainAppPage, name='main app'),
    path('shorten', views.urlShorten, name='url ajax')
]
