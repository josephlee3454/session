from django.urls import path 
from . import views 

urlpatterns = [
        path('', views.session_counter),
        path('delete/', views.session_delete),
        path('count_two/', views.session_counter_2),
]