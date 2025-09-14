from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('pay/<int:id>', views.pay, name='pay'),
    path('success/<int:id>', views.success, name='success'),
]