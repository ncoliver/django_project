from django.urls import path
from .views import HomePageView

app_name = 'feed'

urlpatters = [
    path('', HomePageView.as_view(), name='index'),
]