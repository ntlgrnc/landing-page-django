from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from .forms import FormContacto
from django.core.mail import EmailMessage

# Create your views here.
class HomePageView(TemplateView):

    template_name = "index.html"

    # def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['TituloIni'] = "Hola a todos"
        #context['Titulo2'] = "Otro titulo"
        #return context

    def get (self,request,*args, **kwargs):
        return render(request, self.template_name, {'TituloIni': 'Upline'})

class NosotrosPageView(TemplateView):

    template_name = "nosotros.html"

    def get (self,request,*args, **kwargs):
        return render(request, self.template_name, {'TituloEjemplo': 'Titulo ejemplo'})

#Vista basada en función

def contacto(request):
    formContacto = FormContacto() 

    # Validar que el formulario venga por el metodo POST

    if request.method == "POST":
        formContacto = FormContacto(data = request.POST)
        if formContacto.is_valid():
            nombre = request.POST.get('nombre','')
            asunto = request.POST.get('asunto','')
            correo = request.POST.get('correo','')
            descripcion = request.POST.get('descripcion','')

            # Creamos el objeto con las variables del formulario 
            email = EmailMessage(
                "Upline: tienes un nuevo mensaje",
                "De {} <{}>\n\nEscribió\n\n{}".format(nombre, correo, descripcion),
                "no-contestar@inbox.mailtrap.io",
                ["natagarge@gmail.com"],
                reply_to =[correo]
            )

            # Enviamos el correo:
            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                # No se ha enviado el correo 
                return redirect(reverse('contacto')+"?fail")


    return render(request, 'contacto.html', {'formulario':formContacto})