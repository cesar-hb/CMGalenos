from django.urls import path

from .views import home
from .views import registrar_usuario, iniciar_sesion, cerrar_sesion, ReservarHora
from .views import poblar_bd, acerca_de, contacto, agenda_medico, reporte_informes


urlpatterns = [
    path('', home, name="home"),
    path('registrar_usuario/', registrar_usuario.as_view(), name="registrar_usuario"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('reservar_hora/<action>/<id>', ReservarHora, name="reservar_hora"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('acerca_de/', acerca_de, name="acerca_de"),
    path('contacto/', contacto, name="contacto"),
    path('agenda_medico/', agenda_medico, name="agenda_medico"),
    path('reporte_informes/', reporte_informes, name="reporte_informes"),

]