# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from formtest.form import loginForm


class IndexView(View):
    def get(self, request):
        loginform = loginForm()
        return render(request, 'login.html', {"loginform": loginform})

    def post(self, request):
        loginform = loginForm(request.POST)
        if loginform.is_valid():
            data = loginform.cleaned_data
            user = authenticate(username=data['sname'], password=data['spwd'])
            if user:
                # 用户信息存储
                login(request, user)
                return HttpResponse("登录成功")
            else:
                return HttpResponse("登录失败")
