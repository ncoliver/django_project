from django.urls import path
from .views import HomePageView, PostDetailview, AddPostView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailview.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post'),
]