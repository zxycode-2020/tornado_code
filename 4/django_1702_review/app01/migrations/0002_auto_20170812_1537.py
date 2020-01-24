# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id'], 'verbose_name': '\u5458\u5de5\u4fe1\u606f\u8868', 'verbose_name_plural': '\u5458\u5de5\u4fe1\u606f\u8868'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=30, choices=[(b'1', b'\xe6\xb4\x97\xe5\xa4\xb4'), (b'2', b'\xe6\xb4\x97\xe6\xbe\xa1'), (b'3', b'\xe6\xb4\x97\xe8\x84\x9a')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
    ]
