from django.urls import path
from storing import views

urlpatterns=[
    path('home/',views.createstore,name="home"),
    path('read/',views.readstore,name="read"),
    path('update/<pk>',views.updatestore,name="update"),
    path('delete/<pk>',views.deletestore,name="delete"),
]