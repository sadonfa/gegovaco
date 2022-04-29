from services.models import Services

def get_services(request):

    servs = Services.objects.values_list('id', 'name', 'description', 'info', 'image')

    return {
        'servs': servs
    }