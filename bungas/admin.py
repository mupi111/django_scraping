from django.contrib import admin
from .models import Bunga


# Register your models here.
@admin.register(Bunga)
class BungaAdmin(admin.ModelAdmin):
    list_display = ['image','nama_bunga','harga','detail_image','detail_nama_bunga','detail_harga','sku','kategori']
    list_filter = ('image','nama_bunga','harga','detail_image','detail_nama_bunga','detail_harga','sku','kategori')
    search_fields = ['nama_bunga','kategori']
    list_per_page = 50
