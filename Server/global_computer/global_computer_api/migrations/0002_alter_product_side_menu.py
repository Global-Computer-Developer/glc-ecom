# Generated by Django 4.2.4 on 2023-09-04 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_computer_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='side_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sideMenu', to='global_computer_api.sidemenu'),
        ),
    ]
