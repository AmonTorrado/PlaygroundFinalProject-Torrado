# Generated by Django 4.2.8 on 2023-12-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajo', '0002_curso_entregable_estudiante_profesor_delete_todoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='entregable',
            name='email',
        ),
        migrations.AddField(
            model_name='entregable',
            name='entregado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entregable',
            name='fechadeentrega',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]