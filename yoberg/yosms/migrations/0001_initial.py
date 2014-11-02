# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoscribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.CharField(max_length=34)),
                ('message', models.CharField(max_length=1600)),
                ('sentTo', models.ForeignKey(to='yoscribe.Yoscriber')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
