from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views import View

from .models import Comentario

class Index(View):
    def get(self, request): 
        comentarios = Comentario.objects.order_by("-fecha")
        template = loader.get_template("xss/index.html")
        context = {
            "comentarios": comentarios,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request, *args, **kwargs):
        try:
            nuevo_com = Comentario(texto=request.POST['texto'], nombre=request.POST['nombre'], color=request.POST['color'])
            nuevo_com.save()
            return HttpResponseRedirect("/xss")
        except Exception as e:
            return HttpResponseRedirect("/xss")
