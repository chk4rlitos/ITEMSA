# Generated by Django 3.2 on 2021-04-15 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_auto_20210415_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='telefono_secundario',
            field=models.CharField(max_length=10, null=True, verbose_name='N° Teléfono'),
        ),
    ]