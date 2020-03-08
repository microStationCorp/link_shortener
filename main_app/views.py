from django.shortcuts import render
from .models import SlugTable
from django.http import JsonResponse
# Create your views here.


def mainAppPage(request):
    return render(request, 'main_app/mainApp.html')


def urlShorten(request):
    data = {
        'name': request.GET['slug']
    }
    return JsonResponse(data)
