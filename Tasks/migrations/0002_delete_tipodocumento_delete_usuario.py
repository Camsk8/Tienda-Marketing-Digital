# Generated by Django 5.0 on 2023-12-11 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoDocumento',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
