from datetime import datetime
from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
import datetime
from fallowers.models import Fallower
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=55)
    reg_date = models.DateField(auto_now_add=True)
    article_qty = models.PositiveIntegerField(default=0,editable=False)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return f"{self.name}  Qo'shildi :{self.reg_date}"     




class Article(models.Model):
    name = models.CharField(verbose_name="MAQOLA NOMI",help_text="dssdf sdjdsjfskdfsdfs dshfj", max_length=355,blank=True)
    text = models.TextField(verbose_name="MAQOLA Matni",max_length=8000,default="Text yo'q")
    view = models.PositiveIntegerField(verbose_name="Ko'rishlar soni",default=0 )
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="")
    file = models.FileField(upload_to="audio", blank=True)
    signer = models.ForeignKey('Singer', on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(Category, db_index=True,  on_delete=models.PROTECT)
    reg_date = models.DateField(auto_now_add=True,editable=True )

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def __str__(self):
        return self.name    

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    incomment = models.ForeignKey("Comment",on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Fallower,on_delete=models.CASCADE)
    text = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


class Singer(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55,blank=True)
    image = models.ImageField(upload_to="singers",blank=True)
    info = models.TextField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
   
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



