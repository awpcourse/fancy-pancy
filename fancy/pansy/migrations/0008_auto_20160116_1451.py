# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pansy', '0007_auto_20160116_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to=b'/home/dan/Workspaces/Python Workspace/fancy-pansy/fancy/media'),
        ),
    ]
