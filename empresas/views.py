from django.shortcuts import render, redirect
from .forms import EmpresaForm


def registrar_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_empresas")
    else:
        form = EmpresaForm()
    return render(request, "empresas/registrar_empresa.html", {"form": form})


def lista_empresas(request):
    from .models import Empresa

    empresas = Empresa.objects.all()
    return render(request, "empresas/lista_empresas.html", {"empresas": empresas})
