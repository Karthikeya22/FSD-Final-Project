# Generated by Django 4.0.6 on 2022-08-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KISSAN', '0002_crops_crop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='crops',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
