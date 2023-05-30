from django.urls import path
from .views import TweetView, CreateTweetView, LikeTweetView, UnlikeTweetView, BookmarkTweetView, UnbookmarkTweetView, FollowTweetAuthorView

urlpatterns = [
    path('tweet/<int:tweet_id>/', TweetView.as_view(), name='tweet'),
    path('tweet/create/', CreateTweetView.as_view(), name='create_tweet'),
    path('tweet/<int:tweet_id>/like/', LikeTweetView.as_view(), name='like_tweet'),
    path('tweet/<int:tweet_id>/unlike/', UnlikeTweetView.as_view(), name='unlike_tweet'),
    path('tweet/<int:tweet_id>/bookmark/', BookmarkTweetView.as_view(), name='bookmark_tweet'),
    path('tweet/<int:tweet_id>/unbookmark/', UnbookmarkTweetView.as_view(), name='unbookmark_tweet'),
    path('follow/<int:author_id>/', FollowTweetAuthorView.as_view(), name='follow_author'),
]
