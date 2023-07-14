from django.contrib import admin
from django.urls import path, include
from perfil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),

]
