# Create your models here.
# このモデルでは、 user フィールドは Django の User モデルにリンクする外部キーで、
# どのユーザがツイートを投稿したかを示します。
# url は URL フィールドで、ユーザが共有した URL を格納します。
# created_at フィールドは、ツイートがいつ作成されたかを示す
# datetime フィールドです。
# likes と bookmarks フィールドは、そのツイートに「いいね」やブックマークをしたユーザを示す多対多のフィールドです。

from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='tweet_likes')
    bookmarks = models.ManyToManyField(User, related_name='tweet_bookmarks')

    def __str__(self):
        return self.url
