# Generated by Django 4.1.4 on 2022-12-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prdCreated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
    ]
