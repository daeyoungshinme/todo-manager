from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hellow World!! todo-manager에 오신걸 환영합니다.")

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

