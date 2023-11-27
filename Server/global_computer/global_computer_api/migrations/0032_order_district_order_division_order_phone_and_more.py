# Generated by Django 4.2.5 on 2023-10-07 05:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0031_remove_sidemenu_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='division',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
