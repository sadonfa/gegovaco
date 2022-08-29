from django.shortcuts import render, redirect
from django.http import HttpResponse
import contact
from contact.forms import FormContact
from django.contrib import messages
from contact.models import Contact

# Create your views here.

def cont(request):

    formulario =  FormContact()

    return render(request, 'form_contacto.html',{
        'formulario': formulario
    })

def save_contact(request):
    if request.method == 'POST':
        
        name   = request.POST['name']
        mail = request.POST['mail']
        phone  = request.POST['movil']
        mess = request.POST['message']

        contact = Contact(
            name = name,
            mail = mail,
            phone = phone,
            mess = mess
        )

        contact.save()
        # return HttpResponse(f"Articulo Creado: <strong>{articulo.title}</strong> - {articulo.content}. ")
        messages.success(request, f'Se a enviado tu mensaje, { contact.name }, pronto nos contactaremos.')

        return redirect('contac')
    else:
        return HttpResponse("<h2> No se ha podido crear el articulo</h2> ")
