from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('delete/<int:id>/', views.remove, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
