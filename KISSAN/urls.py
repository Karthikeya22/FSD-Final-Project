from django.urls import path
from KISSAN import views

urlpatterns = [
    path('home1/', views.index, name='home1'),
    path('', views.home, name="index"),
    path('home/', views.analyse, name="home"),
    path('home/result1/', views.Predict, name="prediction"),
    path('home/result1/result/', views.result, name="result"),
]