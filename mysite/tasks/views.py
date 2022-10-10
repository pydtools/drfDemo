import json

from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from django.http import JsonResponse, HttpResponse

# Create your views here.

users = {
    'name': 'Tom',
    'sex': 'male',
    'age': 18
}


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks, })


# @csrf_exempt
# def userList(request):
#     if request.method == 'GET':
#         return JsonResponse(users)
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class UserList(View):
    def get(self, request):
        return JsonResponse(users)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        return JsonResponse(data)
