from django.shortcuts import render, redirect
from .forms import UsuarioForm

def registro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Redirecciona a la vista de éxito
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')
