# Create your models here.
# このモデルでは、user フィールドは Django の User モデルにリンクする外部キーで、
# どのユーザがこの生活記録を作ったかを示します。
# title フィールドは生活記録のタイトルを格納する文字フィールドです。
# content フィールドは生活記録の内容を格納するテキストフィールドです。
# created_atフィールドは、この生活記録がいつ作成されたかを示すdatetimeフィールドである。
# updated_atは、この生活記録が最後に更新されたかを示すdatetimeフィールドでもある。

from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
