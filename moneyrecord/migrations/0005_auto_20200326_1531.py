# Generated by Django 3.0.4 on 2020-03-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyrecord', '0004_auto_20200326_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allmoney',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='时间'),
        ),
    ]
