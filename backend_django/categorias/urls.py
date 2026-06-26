from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria_list),
    path('<int:pk>/', views.categoria_detail),
]