# Generated by Django 3.0.4 on 2020-03-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allmoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now=True, verbose_name='时间')),
                ('money', models.FloatField(verbose_name='金额')),
            ],
            options={
                'verbose_name': '所有money',
            },
        ),
    ]
