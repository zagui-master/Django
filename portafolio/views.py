from django.shortcuts import render
from .models import project
# Create your views here.


def portfolio(request):
    projects = project.objects.all()
    return render(request, "portafolio/portfolio.html", {'projects': projects})
