from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def apiOverview(request):
    return JsonResponse('API BASE', safe=False)
