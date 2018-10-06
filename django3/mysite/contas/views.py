from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    return render(request, 'contas/home.html')

def login(request):
    return render(request, 'contas/login.html')

def registro(request):
    return HttpResponse('Página de Registro')
