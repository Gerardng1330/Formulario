
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
#Para servir archivos estáticos en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.conf.urls.i18n')),
    path("__reload__/", include("django_browser_reload.urls"), name='browser_reload'),
]


urlpatterns += i18n_patterns(
    path(_('adminpaneldjango/'), admin.site.urls),
    path('adminlogin/', include('login.urls'), name='inicio'),
    path('recovery/', include('password.urls'), name='password'),
    path('register/', include('registro.urls'), name='registro'),
    path('', include('formularios.urls'), name='formularios'),
    
    path('', include('formularios.urls')),
    path('en/', include('formularios.urls')),
    path('es/', include('formularios.urls')),
)
if settings.DEBUG:
    #No hacer esto en producción. Esto es solo para el manejo local de archivos estáticos.
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)