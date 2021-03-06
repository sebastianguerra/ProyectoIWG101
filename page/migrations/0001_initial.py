# Generated by Django 3.2.7 on 2021-11-22 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.area')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Realizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicial', models.DateField()),
                ('fecha_last_update', models.DateTimeField()),
                ('resultado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.area')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.IntegerField()),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.pregunta')),
                ('test_realizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.test_realizacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.test'),
        ),
    ]
