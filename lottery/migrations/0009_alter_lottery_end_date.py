# Generated by Django 4.0.4 on 2023-05-19 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0008_alter_lottery_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Fecha de cierre del sorteo', verbose_name='fecha de cierre'),
        ),
    ]
