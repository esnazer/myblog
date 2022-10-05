from django.test import TestCase
from blog.models import Articulo, Categoria

class TestBogModels(TestCase):

    def test_str(self):
        cat_name = Categoria.objects.create(name="Test Name Category")
        cat_description = Categoria.objects.create(description="Test Description Category")
        #art_name = Articulo.objects.create(title="Test Titulo")
        #art_description = Articulo.objects.create(description="Test Description Article")
        #art_cat = Articulo.objects.create(title="Test ManyToMany Article-Category")
        self.assertEqual(str(cat_name),"Test Name Category")
        self.assertEqual(str(cat_description.description),"Test Description Category")

    def test_article_category(self):
        cat1 = Categoria.objects.create(
            name='test_cat1', description='some description cat1')
        cat2 = Categoria.objects.create(
            name='test_cat2', description='some description cat2')
        article = Articulo.objects.create(
            title='linux is a great system',
            description='any one description about this',
        )
        article.categorias.set([cat1.pk,cat2.pk])
        self.assertEqual(article.categorias.count(), 2)

    def test_slug_category(self):
        cat1 = Categoria.objects.create(name='my title 1')
        cat2 = Categoria.objects.create(name='my title 2')
        cat3 = Categoria.objects.create(name='my title 3')
        for n in Categoria.objects.filter(slug__startswith="mytitle"):
            for m in Categoria.objects.filter(slug__startswith="mytitle")[-1:]:
                self.assertNotEqual(n.slug,m.slug)