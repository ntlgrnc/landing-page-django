from django import forms

class FormContacto(forms.Form):
    #Atributos del formulario de contacto

    nombre =  forms.CharField(label= "Nombre", required=True, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu nombre completo'}))
    asunto = forms.CharField(label= "Asunto", required=True, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'¿Porqué nos escribes?'}))
    correo = forms.EmailField(label= "Correo Electrónico", required=True, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico de contacto'}))
    descripcion = forms.CharField(label= "Descripción", required=True, widget=forms.Textarea(attrs={'rows':'3','class':'form-control'}))