from django.db import models

# Create your models here.
# creamos el modelo de la infomecion que tendra nuestra base de datos
# esto es muy impottante ya que nos permite crear los campos donde se guadara la informacion
# title = guarda el nombre de elemto
# link = guarda la url de la pagiana a la cual queremos ir
# icon = guarda el icon en formato de texto
# creadte and updated = son los encargados de gerear las fechas de creacion y modificacion de los elementos


class socialMedia(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    link = models.URLField(
        verbose_name="Link media", null=True, blank=True)
    icon = models.CharField(
        max_length=500, verbose_name="Icono svg o boostrap")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha creado")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha actualizacion")

    class Meta:
        verbose_name = "Redes sociales"
        verbose_name_plural = "Redes sociales"

    def __str__(self):
        return self.title
