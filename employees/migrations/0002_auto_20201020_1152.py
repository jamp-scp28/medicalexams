# Generated by Django 3.0.8 on 2020-10-20 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Ingreso'),
        ),
    ]
