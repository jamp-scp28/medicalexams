# Generated by Django 3.0.8 on 2020-10-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20201020_1152'),
        ('exams_db', '0003_employee_record_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_record',
            name='receipt',
        ),
        migrations.AddField(
            model_name='exams_record',
            name='receipt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.Receipt', verbose_name='FV Examenes'),
        ),
    ]
