
from django.contrib import admin
from django.urls import path
from Calculadora import views



urlpatterns =[
    path('admin/', admin.site.urls),
    path ('',views.index,name='index'),
    path ('newton/',views.newton,name='newton'),
    path ('biseccion/',views.biseccion,name='biseccion'),
    path ('secante/',views.secante,name='secante'),
    path ('newtin_modificado/',views.newton_modificado, name='newton_modificado'),
]
