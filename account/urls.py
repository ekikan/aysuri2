from django.urls import path
from .views import LoginView, RegisterView, ProfileView, EditProfileView, FollowView, UnfollowView, \
    FollowerListView, FollowingListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('follow/<str:username>/', FollowView.as_view(), name='follow'),
    path('unfollow/<str:username>/', UnfollowView.as_view(), name='unfollow'),
    path('followers/<str:username>/', FollowerListView.as_view(), name='followers'),
    path('following/<str:username>/', FollowingListView.as_view(), name='following'),
]
