from django import forms
    
class BusquedaRelojFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)