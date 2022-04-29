from secrets import choice
from django import forms


class FormContact(forms.Form):

    name = forms.CharField(
        label = "Nombre y Apellido"
    )

    mail = forms.EmailField(
        label = "Correo"
    )

    movil = forms.CharField(
        label = "Celular"
    )

    message = forms.CharField(
        label = "Mensaje",
        widget = forms.Textarea
    )

  