from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil vacío
            Perfil.objects.create(user=user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registro.html", {"form": form})
