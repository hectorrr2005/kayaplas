from django.db import models
from django.utils.safestring import mark_safe

class Urun(models.Model):

    class Kdv(float, models.Choices):
        kdv_yok = 0.00, 'Yok'
        kdv_1 = 0.01, 'K.D.V. %1'
        kdv_8 = 0.08, 'K.D.V. %8'
        kdv_18 = 0.18, 'K.D.V. %18'
        
    urun_kodu = models.CharField(max_length=25, unique=True)
    urun_adi = models.CharField(max_length=150)
    urun_yabanci_adi = models.CharField(max_length=150)
    kdv = models.FloatField(choices=Kdv.choices)
    urun_resmi = models.ImageField(upload_to='urunler', blank=True, null=True)

    def urun_thumb(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (
            self.urun_resmi.url)) 