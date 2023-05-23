from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class crops(models.Model) :
    crop_id = models.AutoField
    crop_name = models.CharField(max_length=30)
    crop_image = models.ImageField(upload_to='images', default='')
    description = models.CharField(max_length=500, default='')

    def __str__(self) :
        return self.crop_name