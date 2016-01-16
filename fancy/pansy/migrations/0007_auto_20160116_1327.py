# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pansy', '0006_auto_20160116_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=b'/home/dan/Workspaces/Python Workspace/fancy-pansy/fancy/media'),
        ),
    ]
