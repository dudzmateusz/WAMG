# Generated by Django 3.2.4 on 2021-11-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WAMG', '0010_things_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='things',
            name='photo',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
