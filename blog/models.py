from email.policy import default
from enum import unique
from django.db import models
from django.urls import reverse 
from django.template import defaultfilters
from ckeditor.fields import RichTextField


# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    create = models.DateField(auto_now=False, auto_now_add=True)
    update = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.name

    def save(self, **kwargs):
        if (self.slug == '') or (self.slug == None):       
            tslug = defaultfilters.slugify(self.name)
            tempp = Categoria.objects.filter(slug__startswith=tslug)
            if len(tempp) > 0:
                tslug = defaultfilters.slugify(self.name)+str(len(tempp))
            self.slug = tslug
        else:
            print(self.slug)
        super().save(**kwargs)

class Articulo(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    categorias = models.ManyToManyField(Categoria)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create = models.DateField(auto_now=False, auto_now_add=True)
    update = models.DateField(auto_now=True, auto_now_add=False)

    @property
    def get_absolute_url(self):
        return reverse('articulo-blog', args=(str(self.id)))

    def __str__(self) -> str:
        return self.title

    def save(self, **kwargs): 
        if (self.slug == '') or (self.slug == None):       
            tslug = defaultfilters.slugify(self.title)
            tempp = Articulo.objects.filter(slug__startswith=tslug)
            if len(tempp) > 0:
                tslug = defaultfilters.slugify(self.title)+str(len(tempp))
            self.slug = tslug
        else:
            print(self.slug)
        super().save(**kwargs)