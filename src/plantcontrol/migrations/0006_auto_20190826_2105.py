# Generated by Django 2.2.4 on 2019-08-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantcontrol', '0005_auto_20190826_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='dataUltimaColheita',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
