# Generated by Django 3.1 on 2020-08-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200808_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=models.TextField(),
        ),
    ]
