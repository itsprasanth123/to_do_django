from django.db import models
from django.contrib.auth.models import user
# Create your models here.

class Task(models.model):
    ures=models.ForeignKey(user, on_delete=models.CASCADE, null=true, blank=true)
    title=models.charfield(max_length=200)
    description=models.textfield(null=true, blank=true)
    complete=models.Booleanfield(default=false)
    create=models.datatimefield(auto_naw_add=true)