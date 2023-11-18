from django import forms

class BusquedaTelefonoFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
