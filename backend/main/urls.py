
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
""" Para servir archivos estáticos en desarrollo """
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django_browser_reload.urls import urlpatterns as reload_urls
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language

urlpatterns = [
    path('', include('django.conf.urls.i18n')),
    path("__reload__/", include("django_browser_reload.urls"), name='browser_reload'),
]

urlpatterns += i18n_patterns(
    path(_('adminpaneldjango/'), admin.site.urls),
    path('', include('backend.src_routes.urls'), name='src_urls'),
    path('i18n/', set_language, name='set_language'),
)

if settings.DEBUG:
    #No hacer esto en producción. Esto es solo para el manejo local de archivos estáticos.
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)