# Generated by Django 2.1.5 on 2019-02-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20190209_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainlist',
            name='domain',
            field=models.CharField(max_length=50, unique=True, verbose_name='Domain'),
        ),
    ]
