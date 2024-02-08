from .models import Bunga
from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count
import os

dataBungas = Bunga.objects.all()

var = {'bungas': dataBungas}

# Create your views here.
def dashboard(request):
    count_bunga = Bunga.objects.all().count()
    context = {'count_bunga': count_bunga,}
    return render(request, 'bungas/dashboard.html', context=context)

def search_bunga(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            bungas = Bunga.objects.filter(kategori_contains=query)
            return render(request, 'searchbar.html', {'bunga': bungas}) 
        else:
            print("Gak Ono Data")
            return request(request, 'searchbar.html', {})  

def index(self):
    var['bungas'] = Bunga.objects.values('id','image','nama_bunga','harga','detail_image','detail_nama_bunga','detail_harga','sku','kategori').\
    order_by('id')
    return render(self, 'bungas/index.html', context=var)

class DetailBunga(DetailView):
    model = Bunga
    template_name = 'bungas/detail.html'
    
    def get_context_data(self, **kwargs):
        context = var
        context.update(super().get_context_data(**kwargs))
        return context

def addBunga(request):
        if request.method == "POST":
            bungas = Bunga()
            bungas.nama_bunga = request.POST.get('nama_bunga')
            bungas.harga = request.POST.get('harga')
            bungas.sku = request.POST.get('sku')
            bungas.kategori = request.POST.get('select_kategori')
                
                
            if len(request.FILES) != 0:
                bungas.image = request.FILES['image']
                    
            bungas.save()
            messages.success(request, 'Produk berhasil ditambahkan')
            return redirect('/bungas')
        return render(request, 'bungas/add.html')
    
def updateBunga(request, pk):
    bungas = Bunga.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(bungas.image)>0:
                os.remove(bungas.image.path)
            bungas.image = request.FILES['gambar_produk']
        bungas.nama_bunga = request.POST.get('nama_bunga')
        bungas.harga = request.POST.get('harga')
        bungas.sku = request.POST.get('sku')
        bungas.kategori = request.POST.get('select_kategori')
        bungas.save()
        messages.success(request, 'Produk berhasil diupdate')
        return redirect('/bungas')
    context = {'bungas':bungas}
    return render(request, 'bungas/update.html', context)

class DeleteBunga(DeleteView):
    model = Bunga
    template_name = 'bungas/delete.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = var
        context.update(super().get_context_data(**kwargs))
        return context


