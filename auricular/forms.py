from django import forms
    
class BusquedaAuricularFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)