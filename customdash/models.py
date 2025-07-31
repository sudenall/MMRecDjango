from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings #we import settings to use AUTH_USER_MODEL

def user_dataset_path(instance, filename):    #converts the ID of the user who uploaded the file to the folder name, we separate the user's file into subfolders with user_id
    return f'datasets/user_{instance.user.id}/{filename}'


class CustomDataset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_dataset_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"  #it's for the making this model readable when it appears in the admin panel or shell

# Create your models here.
