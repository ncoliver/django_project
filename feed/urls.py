from django.urls import path
from .views import HomePageView, PostDetailview

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailview.as_view(), name='detail'),
]