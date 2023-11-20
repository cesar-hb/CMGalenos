from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate
from .forms import ReservarHora, IniciarSesionForm, RegistroForm
from django.views.decorators.csrf import csrf_exempt
from .models import AtencionMedica
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, "cmg/home.html") 

class registrar_usuario(CreateView):
    model = User
    template_name = "cmg/registrar_usuario.html"
    form_class = RegistroForm
    success_url = reverse_lazy('iniciar_sesion')

def iniciar_sesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(home)
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "cmg/iniciar_sesion.html", data)

def cerrar_sesion(request):
    logout(request)
    return redirect(home)

def ReservarHora(request, action, id):
    data = {"mesg": "", "form": AtencionMedica, "action": action, "id": id}


    if action == 'ins':
        if request.method == "POST":
            form = AtencionMedica(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡Se ha gestionado la reserva exitosamente!"
                except:
                    data["mesg"] = "Ha ocurrido un error al ingresar la reserva"


    elif action == 'upd':
        objeto = AtencionMedica.objects.get(id=id)
        if request.method == "POST":
            form = ReservarHora(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡Se ha actualizado la hora correctamente!"
        data["form"] = ReservarHora(instance=objeto)


    elif action == 'del':
        try:
            AtencionMedica.objects.get(id=id).delete()
            data["mesg"] = "¡La hora se ha eliminado correctamente"
            return redirect(AtencionMedica, action='ins', id = '-1')
        except:
            data["mesg"] = "¡No existe tal hora!"


    data["list"] = AtencionMedica.objects.all().order_by('id')
    return render(request, "cmg/reservar_hora.html", data)