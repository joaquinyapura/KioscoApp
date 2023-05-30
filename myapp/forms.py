from django import forms


class CrearCliente(forms.Form):
    nombre = forms.CharField(label='nombre del cliente')
    importe = forms.IntegerField()
