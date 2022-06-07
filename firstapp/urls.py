from django.urls import path

from firstapp import views

urlpatterns = [
    path('', views.hellodjango),
    path('date/', views.fulldate),
    path('date/<str:index>/', views.date),
    path('<str:name>/', views.helloname),
]