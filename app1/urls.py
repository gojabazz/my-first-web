from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('mobin/',views.mobin),
    path('rafi/',views.rafi),
]
