from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import Tweet


class TweetView(View):
    def get(self, request, tweet_id):
        # ここでウェブサイト表示ロジックを処理する必要があります
        pass


class CreateTweetView(View):
    def post(self, request):
        # ここでウェブサイト共有ロジックを処理する必要があります
        pass


class LikeTweetView(View):
    def post(self, request, tweet_id):
        # ここで「いいね」ロジックを処理する必要があります
        pass


class UnlikeTweetView(View):
    def post(self, request, tweet_id):
        # ここで「いいね取り消し」ロジックを処理する必要があります
        pass


class BookmarkTweetView(View):
    def post(self, request, tweet_id):
        # ここでブックマークロジックを処理する必要があります
        pass


class UnbookmarkTweetView(View):
    def post(self, request, tweet_id):
        # ここでブックマーク取り消しロジックを処理する必要があります
        pass


class FollowTweetAuthorView(View):
    def post(self, request, author_id):
        # ここでツイート作者のフォローロジックを処理する必要があります
        pass
