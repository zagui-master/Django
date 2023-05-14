
from .models import socialMedia
from django.shortcuts import render, HttpResponse

# socialMedia trae la data de la base de datos y se los pasamos a las vistas
# para poderlos usar


def home(request):
    linkMedia = socialMedia.objects.all()
    return render(request, 'core/home.html', {'linkMedia': linkMedia})


def contact(request):
    linkMedia = socialMedia.objects.all()
    return render(request, "core/contact.html", {'linkMedia': linkMedia})


def about(request):
    linkMedia = socialMedia.objects.all()
    return render(request, "core/about.html", {'linkMedia': linkMedia})
