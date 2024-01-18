from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
import os

class DonationType(models.Model):
    title = models.CharField(("İsim"), max_length=50)
    def __str__(self):
        return self.title
    
class Donations(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kim Bağış Yaptı"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(("Nekadar Bağış Yapıldı"))
    donation_type = models.ForeignKey(DonationType, verbose_name=("Aylık / Tek Seferlik Ödeme"), on_delete=models.CASCADE)
    created_date = models.DateField(("Eklenme tarihi"), auto_now_add=True)
    updated_date = models.DateField(("Güncellenme tarihi"), auto_now=True)
    def __str__(self):
        return f'{self.user.username} tarafından {self.quantity} TL bağış yapıldı Bağış Tipi {self.donation_type.title}'
        
def image_dir_path(instance, filename):
    chapter = instance.slug
    return os.path.join(chapter, filename)


class blog(models.Model):
    author = models.ForeignKey(User, verbose_name=("yazar"), on_delete=models.CASCADE)
    cover_image = models.ImageField(("kapak resmi"), upload_to=image_dir_path, )
    title = models.CharField(("title"), max_length=150)
    slug = models.SlugField(default = 'Slug ismi')
    content = RichTextField()
    created_date = models.DateTimeField( auto_now_add=True)
    updated_date = models.DateTimeField( auto_now=False)
    active = models.BooleanField(("aktifmi"))
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blogdetail", kwargs={"id": self.pk})
    
