
from django.contrib import admin
from django.urls import path
#from . import views
from core import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('about/', views.about, name="about"),
    # path('index/', views.index),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
