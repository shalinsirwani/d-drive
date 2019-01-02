from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Fls(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User , on_delete=models.CASCADE) 
    uploaded_at = models.DateTimeField(auto_now_add=True)
   

    def delete(self , *args , **kwargs):
        self.file.delete()
        super().delete(*args , **kwargs)
