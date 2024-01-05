from .import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
]
    #path('',views.demo1,name='demo1'),
    #path('home/',views.Arithoperation,name="Arithoperation"),
   # path('sub/', views.subtraction,name="subtraction"),
    #path('mul/', views.multiplication, name="multiplication"),
    #path('div/', views.division, name="division"),


