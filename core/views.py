from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    return render(request,'core/index.html')
