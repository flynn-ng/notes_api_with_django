from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('notes/', views.get_notes),
    path('notes/create/', views.create_note),
    path('notes/<str:pk>/update/', views.update_note),
    path('notes/<str:pk>/delete/', views.delete_note),
    path('notes/<str:pk>/', views.get_note),  # <str:pk> dynamic parameter
]
