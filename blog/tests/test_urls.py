from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog.views import BlogView, ArticuloView, CategoriasView

class TestUrls(SimpleTestCase):

    def test_blog_url_resolved(self):
        url = reverse('articulo-blog')
        self.assertEqual(resolve(url).func.view_class, ArticuloView)

    def test_blog_url_resolved(self):
        url = reverse('categorias-blog')
        self.assertEqual(resolve(url).func.view_class, CategoriasView)