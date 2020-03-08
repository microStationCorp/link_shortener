from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainAppPage, name='main app'),
    path('shorten', views.urlShorten, name='url ajax'),
    path('slugValidation', views.slugQuery, name='slug validation'),
    path('go/<str:slug>', views.urlRedirect, name='redirect')
]
