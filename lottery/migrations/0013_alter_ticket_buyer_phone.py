# Generated by Django 4.0.4 on 2023-05-21 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0012_remove_ticket_buyer_email_ticket_buyer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='buyer_phone',
            field=models.BigIntegerField(blank=True, help_text='Teléfono del comprador del boleto', null=True, verbose_name='teléfono'),
        ),
    ]
