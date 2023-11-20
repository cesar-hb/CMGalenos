from django.urls import path

from .views import home
from .views import registrar_usuario, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('', home, name="home"),
    path('registrar_usuario/', registrar_usuario.as_view(), name="registrar_usuario"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),

]