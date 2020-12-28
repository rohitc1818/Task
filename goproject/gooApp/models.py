from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=20,default='')
    image = models.ImageField(upload_to='upload/images/', null=False)
    phone = models.IntegerField()
    Email = models.EmailField(max_length=254)
    bio = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.name


