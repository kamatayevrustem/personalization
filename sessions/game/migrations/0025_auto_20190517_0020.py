# Generated by Django 2.1.5 on 2019-05-17 00:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20190517_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playergameinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 17, 0, 20, 4, 222099)),
        ),
    ]
