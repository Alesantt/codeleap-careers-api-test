from django.contrib import admin
from django.urls import path
from careers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('careers/', views.post_list_create),
    path('careers/<int:pk>/', views.post_update_delete),
    path('careers/<int:pk>/like/', views.like_post),
]