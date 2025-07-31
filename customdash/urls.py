from django.urls import path
from . import views

urlpatterns = [
    path('add-model/', views.add_model_page, name='customdash_add_model'),
    path('upload-dataset/', views.upload_dataset, name='upload_dataset'),
]