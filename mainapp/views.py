from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):

    # return HttpResponse('<h1> inicio </h1>')
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })