# Generated by Django 3.2 on 2021-04-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personal',
            options={'ordering': ['tipo_trabajador'], 'verbose_name': 'Personal', 'verbose_name_plural': 'Personal'},
        ),
        migrations.AddField(
            model_name='persona',
            name='estado_civil',
            field=models.BooleanField(default=False, verbose_name='Estado Civil'),
        ),
    ]