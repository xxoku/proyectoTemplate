from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    return render(request, 'templateApp/holamundo.html')


def renderTemplate2(request):
    data = {"nombre" : "Benjamin"}
    return render(request, 'templateApp/holamundo2.html', data)

def userTemplate(request):
    data = {"ID" : "123", "nombre" : "Clark Kent", "Email" : "superman@jl.org" }
    return render(request, 'templateApp/infousuario.html', data)

