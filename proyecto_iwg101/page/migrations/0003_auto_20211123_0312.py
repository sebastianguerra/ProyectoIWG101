# Generated by Django 3.2.7 on 2021-11-23 03:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20211123_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_realizacion',
            name='fecha_inicial',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='test_realizacion',
            name='fecha_last_update',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
