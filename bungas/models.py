from django.db import models
from django.urls import reverse
import os

# Create your models here.

def filepath(request, filename):
    return os.path.join('uploads/', filename)


class Bunga(models.Model):
    KT_CHOICES = (
        ('Pacar Air (Balsam)','Benih Pacar Air (Balsam)'),('Mr Fothergills',' Benih Mr Fothergills'),('Larkspur & Delphinium','Benih Larkspur & Delphinium'),
        ('Buddleja (Butterfly Bush)','Benih Buddleja (Butterfly Bush)'),('Nasturtium','Benih Nasturtium'),('Bayam','Benih Bayam'),('Jagung','Benih Jagung'),('Cosmos','Benih Cosmos'),
        ('Bit Merah','Benih Bit Merah'),('Semangka','Benih Semangka'),('Bintang Asia','Benih Bintang Asia'),('Labu','Benih Labu'),('Berkebun','Perlengkapan Berkebun'),
        ('Hidroponik','Tanaman Hidroponik'),('Herbisida','Tanaman Herbisida'),('Bunga Matahari (Sunflower)','Bebih Bunga Matahari (Sunflower)')
    )
  
    image = models.ImageField(upload_to='filepath', blank=True, null=True)
    nama_bunga = models.CharField('Nama Bunga', max_length=100)
    harga = models.CharField('Harga (Rp)', max_length=100)
    detail_image = models.ImageField(upload_to='filepath', blank=True, null=True)
    detail_nama_bunga =models.CharField('Detail Nama Bunga', max_length=100)
    detail_harga =  models.CharField('Harga (Rp)', max_length=100)
    sku = models.CharField('Detail SKU', max_length=50)
    kategori = models.CharField('Kategori', max_length=50, choices=KT_CHOICES)
    

def _str_(self):
    return self.nama_bunga

def get_absolute_url(self):
    return reverse('home_page')