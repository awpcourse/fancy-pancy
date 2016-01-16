# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pansy', '0002_remove_photo_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TagToPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='tagtophoto',
            name='photo',
            field=models.ForeignKey(to='pansy.Photo'),
        ),
        migrations.AddField(
            model_name='tagtophoto',
            name='tag',
            field=models.ForeignKey(to='pansy.Tag'),
        ),
    ]
