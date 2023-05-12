
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portafolio import views as portafolio_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('contact/', core_views.contact, name="contact"),
    path('portfolio/', portafolio_views.portfolio, name="portfolio"),
    path('about/', core_views.about, name="about"),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
