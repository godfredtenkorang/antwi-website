# Generated by Django 4.1 on 2022-10-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepost',
            name='image',
            field=models.ImageField(default='', upload_to='home_post'),
        ),
    ]