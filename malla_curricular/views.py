from django.shortcuts import render
from .forms import CarreraForm
# Create your views here.

def CrearCarrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
    form = CarreraForm()
    return render(request, 'crear_carrera.html', {'form': form})
