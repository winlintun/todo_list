from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
	path('', views.home, name="home"),
	path('add/', views.add_item, name="add_item"),
	path('delete/<int:item_id>/', views.delete_item, name="delete_item"),
	path('register/', views.singup, name='singup'),
	path('login/', views.singin, name='singin'),
	path('logout/', views.singout, name='logout'),
]