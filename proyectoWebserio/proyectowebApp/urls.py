from django.urls import path

from proyectowebApp import views


urlpatterns = [
    
    path('', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('contacto/', views.contacto, name="Contacto"),
    path('blog/', views.blog, name="Blog"),
    
]


