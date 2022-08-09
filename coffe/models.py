from django.db import models

# Create your models here.
class Coffe(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name="Info")
    
    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = "Food menu "
        verbose_name_plural= "Foods menu"
