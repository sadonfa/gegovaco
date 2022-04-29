from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from services.models import Services

# Create your views here.


def services(request, id_service):

    services_id = get_object_or_404 (Services, pk=id_service)

    # return HttpResponse('<h1> Servicios </h1>')
    return render(request, 'services/service.html', {
        'services_id': services_id
    })