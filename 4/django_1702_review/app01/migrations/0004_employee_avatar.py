# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20170812_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to=b'avatar/'),
            preserve_default=False,
        ),
    ]
