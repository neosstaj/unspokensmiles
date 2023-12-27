from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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

