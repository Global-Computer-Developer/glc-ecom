# Generated by Django 4.2.5 on 2023-09-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0015_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]