from django.db import models
from django.db.models.signals import pre_save
from .utils import *



class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    author_name=models.CharField(max_length=100,blank=True)
    title=models.TextField(max_length=200)
    body=models.TextField()
    slug=models.SlugField(max_length=200,unique=True)
    comment=models.TextField()
    comment_name= models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/", blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)+" "+str(self.id)



def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Blog)



