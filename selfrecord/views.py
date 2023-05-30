from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View
from .models import Record


class RecordView(View):
    def get(self, request, record_id):
        # ここでノート表示ロジックを処理する必要があります
        pass


class CreateRecordView(View):
    def post(self, request):
        # ここでノート作成ロジックを処理する必要があります
        pass


class EditRecordView(View):
    def post(self, request, record_id):
        # ここでノート編集ロジックを処理する必要があります
        pass


class DeleteRecordView(View):
    def post(self, request, record_id):
        # ここでノート削除ロジックを処理する必要があります
        pass
