# Generated by Django 3.0.4 on 2020-03-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyrecord', '0007_allmoney_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmoney',
            name='cause',
            field=models.CharField(default='默认值', max_length=50, verbose_name='原因'),
        ),
        migrations.AddField(
            model_name='allmoney',
            name='degree',
            field=models.IntegerField(default=0, verbose_name='等级'),
        ),
    ]
