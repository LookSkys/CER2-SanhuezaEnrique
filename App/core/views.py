from django.shortcuts import render
from core.models import correspondencia

def home(request):
    busqueda = request.POST.get("buscar")
    correspondencias = correspondencia.objects.all()
    
    if busqueda:
        correspondencias = correspondencia.objects.filter(num_res = busqueda)
    return render(request,"core/home.html",{"correspondencias":correspondencias})

def base(request):
    return render(request,"core/base.html")