
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
urlpatterns = [
     path(_('admin/'), admin.site.urls),
    path('',include('login.urls')),
    path('',include('password.urls')),
    path('',include('registro.urls')),
    path('en/', include('formularios.urls')),
    path('es/', include('formularios.urls')),
   

    
]
urlpatterns += i18n_patterns(
    
    path('', include('formularios.urls')),
   
)
