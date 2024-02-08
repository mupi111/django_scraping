from django.urls import path
from .views import index
from .views import dashboard
from .views import search_bunga
from .views import DetailBunga
from .views import addBunga
from .views import updateBunga
from .views import DeleteBunga

urlpatterns = [
    path('', dashboard, name='homepage'),
    path('bungas', index, name='index'),
    path('search/', search_bunga, name='search'),
    path('bungas/<int:pk>', DetailBunga.as_view(), name='detail'),
    path('bungas/create', addBunga, name='add'),
    path('bungas/edit/<int:pk>', updateBunga, name='edit'),
    path('bungas/delete/<int:pk>', DeleteBunga.as_view(), name='delete')


]
