# Generated by Django 4.2.7 on 2024-01-15 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]