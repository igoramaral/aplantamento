# Generated by Django 2.2.4 on 2019-08-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umidade', models.BooleanField()),
                ('temperatura', models.FloatField()),
                ('luz', models.BooleanField()),
                ('dataMedicao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
