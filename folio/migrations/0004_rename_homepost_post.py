# Generated by Django 4.1 on 2022-10-27 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0003_alter_homepost_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePost',
            new_name='Post',
        ),
    ]