# Generated by Django 4.2.5 on 2023-09-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0024_rename_category_slug_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='avg_star',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='reviews',
            name='total_review',
            field=models.IntegerField(default=0),
        ),
    ]