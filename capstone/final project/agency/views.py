from django.shortcuts import render
from django.http import HttpResponse
from .models import Plan

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    context = {}
    return render(request, 'index.html', context=context)

def plans(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    plans = Plan.objects.all()

    context = {
        'plans': plans
    }
    return render(request, 'plans.html', context=context)

def blog(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    context = {}
    return render(request, 'blog.html', context=context)

def about(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    context = {}
    return render(request, 'about.html', context=context)
