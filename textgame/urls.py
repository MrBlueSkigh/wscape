from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartingScreen, name='StartingScreen'),
    path('load/', views.LoadScreen.as_view(), name='LoadScreen'),
    path('create/', views.LoginScreen.as_view(), name='LoginScreen'),
    path('<int:pk>/', views.genericRoom.as_view(), name='genericRoom'),
]

