# Generated by Django 4.2.4 on 2023-09-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0003_alter_product_side_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model_name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
