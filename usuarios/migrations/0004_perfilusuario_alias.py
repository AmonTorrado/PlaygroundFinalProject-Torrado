# Generated by Django 4.2.7 on 2024-01-15 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_perfilusuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='alias',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]