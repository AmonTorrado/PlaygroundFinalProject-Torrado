# Generated by Django 4.2.7 on 2024-01-15 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=0, upload_to='imagenes_productos'),
            preserve_default=False,
        ),
    ]