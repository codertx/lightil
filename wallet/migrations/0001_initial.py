# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=20)),
                ('consum_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.FloatField()),
                ('name', models.CharField(max_length=10)),
                ('icon', models.CharField(max_length=10)),
                ('credit_card', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='transfer',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_wallet', to='wallet.Wallet'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_wallet', to='wallet.Wallet'),
        ),
        migrations.AddField(
            model_name='consum',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet'),
        ),
    ]