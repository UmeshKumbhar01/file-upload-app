from django.db import models


class YourModel(models.Model):
    file = models.FileField(upload_to='uploads/')
