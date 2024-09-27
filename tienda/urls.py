from django.conf import settings
from django.urls import path, include
from . import views
from django.contrib import admin
from .views import Producto

app_name='core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
