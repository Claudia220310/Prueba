from django.urls import path
from .views import registro, registro_exitoso

urlpatterns = [
    path('', registro, name='registro'),
    path('registro_exitoso/', registro_exitoso, name='registro_exitoso'),
]
