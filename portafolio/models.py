from django.db import models


class project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    picture = models.ImageField(verbose_name="Imagen", upload_to='projects')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha creado")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha actualizacion")
    link = models.URLField(verbose_name="Direccion web", null=True, blank=True)
    price = models.CharField(max_length=20, verbose_name="Precio")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.title
