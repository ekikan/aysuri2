from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import User


class LoginView(views.LoginView):
    def post(self, request):
        # ここでログインロジックを処理する必要があります
        pass


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == "HAN" and password == "8921055":
        # return HttpResponse("ログインしました")
        return redirect("http://127.0.0.1:8000/user/list")

    # return HttpResponse("ログイン失敗しました")
    return render(request,"login.html", {"error_msg": "ログイン失敗しました"})


class RegisterView(CreateView):
    template_name = ''
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)


class ProfileView(DetailView):
    template_name = ""
    def get(self, request, username):
        # ここで個人ホームページの表示ロジックを処理する必要があります
        pass


class EditProfileView(View):
    def post(self, request, username):
        # ここで個人情報編集ロジックを処理する必要があります
        pass


class FollowView(View):
    def post(self, request, username):
        # ここでフォローロジックを処理する必要があります
        pass


class UnfollowView(View):
    def post(self, request, username):
        # ここでアンフォローロジックを処理する必要があります
        pass


class FollowerListView(View):
    def get(self, request, username):
        # ここでフォロワーリスト表示ロジックを処理する必要があります
        pass


class FollowingListView(View):
    def get(self, request, username):
        # ここでフォローリスト表示ロジックを処理する必要があります
        pass
