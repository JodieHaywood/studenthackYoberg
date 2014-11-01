# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yoscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yoname', models.CharField(unique=True, max_length=200)),
                ('phonenumber', models.CharField(unique=True, max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
