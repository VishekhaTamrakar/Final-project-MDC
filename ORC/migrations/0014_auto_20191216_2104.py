# Generated by Django 2.1.5 on 2019-12-17 03:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0013_auto_20191214_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_enddate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 3, 4, 0, 51641, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_startdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 3, 4, 0, 51615, tzinfo=utc)),
        ),
    ]