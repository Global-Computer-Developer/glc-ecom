# Generated by Django 4.2.5 on 2023-10-05 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0030_sidemenu_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidemenu',
            name='position',
        ),
    ]