from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate
from .forms import AtencionMedica, IniciarSesionForm, RegistroForm
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