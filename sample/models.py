from django.db import models

# Create your models here.
class TodoManagerUser(models.Model):
    id_user = models.CharField(max_length=20)
    nm_user = models.CharField(max_length=20)
    email_user = models.CharField(max_length=30)
    cell_number = models.CharField(max_length=15)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
