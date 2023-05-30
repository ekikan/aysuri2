# Create your views here.

from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        # ここでホームページの表示ロジックを処理する必要があります
        return render(request, 'welcome/home.html')
