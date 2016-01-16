# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pansy', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='path',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=b'https://images.unsplash.com/photo-1450101215322-bf5cd27642fc?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&w=1080&fit=max&s=eb4214b1bb04674628992a705ad3dc30', upload_to=b'/home/dan/Workspaces/Python Workspace/fancy-pansy/fancy/media'),
        ),
    ]
