from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hellow World!! todo-manager에 오신걸 환영합니다.")
