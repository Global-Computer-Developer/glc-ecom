# Generated by Django 4.2.5 on 2023-09-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0019_alter_brand_slug_alter_sidemenu_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]
