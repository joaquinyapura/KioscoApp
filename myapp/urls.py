from . import views


from django.urls import path

urlpatterns = [
    path('', views.hello),
    path('productos/', views.productos),
    path('nuevocliente/', views.nuevo_cliente)
]
