from django.contrib import admin
from .models import socialMedia

# la clase ProjectMedia se encaga de renderizar o mostrar la hora de ceacion y  modicacion de cada elemnto
# admin.site.register(socialMedia, ProjectMedia) = se encarga de mostrar la tabla en el admin


class ProjectMedia(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(socialMedia, ProjectMedia)
