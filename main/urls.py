
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
#Para servir archivos estáticos en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path(_('admin/'), admin.site.urls),
    path('',include('login.urls')),
    path('',include('password.urls')),
    path('',include('registro.urls')),
    
    #django browser reload
    path("__reload__/", include("django_browser_reload.urls")),
    
]

urlpatterns += i18n_patterns(
    path('', include('formularios.urls')),
    path('en/', include('formularios.urls')),
    path('es/', include('formularios.urls')),
)

if settings.DEBUG:
    #No hacer esto en producción. Esto es solo para el manejo local de archivos estáticos.
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
