from django.shortcuts import render
from .models import project
from core.models import socialMedia

# project como socialMedia traen la data de la base de datos y se los pasamos a la vista portafolio
# para poderlos usar


def portfolio(request):
    projects = project.objects.all()
    linkMedia = socialMedia.objects.all()
    return render(request, "portafolio/portfolio.html", {'projects': projects, 'linkMedia': linkMedia})
