from django.db import models

class UploadFile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    book = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    file = models.FileField(upload_to='image')
    upload_at = models.DateTimeField(auto_now_add=True)