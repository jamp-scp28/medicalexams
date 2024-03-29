# Generated by Django 3.0.8 on 2020-09-21 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['payment_day', 'payment_amount']},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='balance_from_previous_term',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='class_for',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='session',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='student',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='term',
        ),
        migrations.AddField(
            model_name='invoice',
            name='enterprise',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_link',
            field=models.FileField(blank=True, upload_to='finance/payments/'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='provider',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
