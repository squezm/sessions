# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg_board', '0004_board_choice_poll_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board_choice_poll',
            name='votes',
        ),
    ]
