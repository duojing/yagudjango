# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=100)),
                ('block_img', models.ImageField(default='None/no_img.png', upload_to='/')),
                ('view_img', models.ImageField(default='None/no_img.png', upload_to='/')),
                ('block_info', models.TextField(help_text='블럭기본정보입력', verbose_name='블럭정보')),
                ('block_tip', models.TextField(help_text='블럭별 팁을 입력', verbose_name='Tip!')),
            ],
        ),
        migrations.DeleteModel(
            name='Baseball',
        ),
    ]
