from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('', RedirectView.as_view(url='/tareas/')),  # Redirige la raíz a /tareas/
    path('accounts/', include('django.contrib.auth.urls')),
]
