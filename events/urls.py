from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    # Landing page
    path('', views.landing_page, name='landing_page'),
]
