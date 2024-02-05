
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
    path(_('admin/'), admin.site.urls, name='admin django'),
    path('login/', include('login.urls'), name='login'),
    path('password/', include('password.urls'), name='password'),
    path('registro/', include('registro.urls'), name='registro'),
    path('', include('formularios.urls'), name='formularios'),
    
    path('', include('formularios.urls')),
    path('en/', include('formularios.urls')),
    path('es/', include('formularios.urls')),
)