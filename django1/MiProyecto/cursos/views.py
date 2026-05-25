from django.shortcuts import render

# Create your views here.

def mostrarForm(request):
    resultado = 0
    if request.method == 'POST':
        n1 = int(request.POST['n1'])
        n2 = int(request.POST['n2'])        
        resultado = n1+n2

    context = {
        'resultado':resultado
    }

    return render(request,'formulario.html',context)