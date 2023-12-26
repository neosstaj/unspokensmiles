from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Donations(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kim Bağış Yaptı"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(("Nekadar Bağış Yapıldı"))
    def __str__(self):
        return f'{self.user.username} tarafından {self.quantity} TL bağış yapıldı'

