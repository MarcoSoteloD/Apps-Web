from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.shortcuts import render, redirect 

# Create your views here.
def landing(request):
    a= pan.objects.all()
    print(a)
    m=panecito
    context={
        'pan':panecito,
    }
    return render (request,'hijo.html',context)
#--------------------------------------------------------------------------------

def post_agregar(request):
    if request.method == "POST":
        form = panecito(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("formato valido")
            
        return redirect('landing')
#--------------------------------------------------------------------------------

def modificar(request):
    # Consulta todos los registros de la base de datos
    panes = pan.objects.all()
    # Pasa los registros a un template para su renderizado
    return render(request, 'modificar.html', {'panes': panes})
#--------------------------------------------------------------------------------

def modificar_pan(request, pk):
    # Obtiene el objeto Pan con la clave primaria pk. Si no se encuentra, devuelve un error 404.
    Pan = get_object_or_404(pan, pk=pk)  # Pan
    
    if request.method == 'POST':
        # Si la solicitud es un POST, crea un formulario panecito con los datos de la solicitud y la instancia de Pan.
        form = panecito(request.POST, instance=Pan)
        # Verifica si el formulario es válido.
        if form.is_valid():
            # Guarda los cambios en el formulario en la base de datos.
            form.save()
            # Redirige al usuario a la URL almacenada en la variable de sesión 'modificar', 
            # que es la página anterior o la raíz si no hay una página anterior almacenada.
            return redirect(request.session.get('modificar', '/'))  # Redirige a la página anterior o a la raíz si no hay una página anterior almacenada
    else:
        # Si la solicitud no es un POST, crea un formulario panecito con la instancia de Pan.
        form = panecito(instance=Pan)
    
    # Guarda la URL actual en la variable de sesión 'modificar' para que pueda ser utilizada en redirecciones posteriores.
    request.session['modificar'] = request.META.get('HTTP_REFERER', '/')
    
    # Renderiza el template 'modificar_pan.html' con el formulario.
    return render(request, 'modificar_pan.html', {'form': form})
#--------------------------------------------------------------------------------


def calc(request):
    return render(request,'calculadora.html')