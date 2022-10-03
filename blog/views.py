from django.shortcuts import render
from django.views import View
from blog.models import Articulo

# Create your views here.
class ArticuloView(View):
    def get(self, request, **kwargs):
        id = kwargs['id']
        article = Articulo.objects.filter(ipk=id).first()
        parameters = {}
        return render(request, 'blog/articulo.html', parameters)