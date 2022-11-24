from django import forms
from blog.models import Articulo, Categoria

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('title', 'description', 'categorias')
        labels = {
            'title': 'Titulo:',
            'description': 'Descripcion:',
            'categorias': 'Categorias:',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('name','description')
        labels = {
            'name': 'Nombre:',
            'description': 'descripción'
        }
