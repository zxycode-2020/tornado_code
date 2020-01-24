# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.BooleanField(choices=[(1, b'\xe7\x94\xb7'), (0, b'\xe5\xa5\xb3')])),
                ('department', models.CharField(max_length=30, choices=[(1, b'\xe6\xb4\x97\xe5\xa4\xb4'), (2, b'\xe6\xb4\x97\xe6\xbe\xa1'), (3, b'\xe6\xb4\x97\xe8\x84\x9a')])),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_modi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
