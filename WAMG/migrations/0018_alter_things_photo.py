# Generated by Django 3.2.4 on 2021-11-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WAMG', '0017_alter_things_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='things',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.query_utils.DeferredAttribute object at 0x0000026511E4DA60>/'),
        ),
    ]
