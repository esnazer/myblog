from django.db import models
from django.urls import reverse 

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create = models.DateField(auto_now=False, auto_now_add=True)
    update = models.DateField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])