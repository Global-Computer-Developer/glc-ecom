# Generated by Django 4.2.5 on 2023-09-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0027_remove_reviews_total_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='total_review',
            field=models.IntegerField(default=0),
        ),
    ]
