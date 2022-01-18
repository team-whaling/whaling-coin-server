from django.contrib import admin
from .models import Cryptocurrency
# Register your models here.
@admin.register(Cryptocurrency)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['coin_code', 'coin_fullname', 'coin_image', 'full_updated_time', 'updated_date', 'updated_time']
    list_display_links = ['coin_code']
    list_editable = ['coin_image']