from django.contrib.admin import ModelAdmin, register

from urunler.models import Urun


@register(Urun)
class UrunAdmin(ModelAdmin):
    list_display = ('urun_kodu', 'urun_adi', 'urun_yabanci_adi', 'kdv')