# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg_board', '0003_remove_board_choice_poll_experience_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_choice_poll',
            name='votes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
