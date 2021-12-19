from django.shortcuts import render

# Create your views here.

def dashboard(request):
    template = "dashboard/main.html"
    context = {}

    return render(request, template, context)   
