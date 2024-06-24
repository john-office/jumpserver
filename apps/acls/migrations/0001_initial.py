# Generated by Django 4.1.13 on 2024-05-09 03:16

import common.db.fields
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandFilterACL',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('priority', models.IntegerField(default=50, help_text='1-100, the lower the value will be match first', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Priority')),
                ('action', models.CharField(default='reject', max_length=64, verbose_name='Action')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('users', common.db.fields.JSONManyToManyField(default=dict, to='users.User', verbose_name='Users')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('assets', common.db.fields.JSONManyToManyField(default=dict, to='assets.Asset', verbose_name='Assets')),
                ('accounts', models.JSONField(default=list, verbose_name='Accounts')),
            ],
            options={
                'verbose_name': 'Command acl',
                'ordering': ('priority', '-is_active', 'name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommandGroup',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('type', models.CharField(choices=[('command', 'Command'), ('regex', 'Regex')], default='command', max_length=16, verbose_name='Type')),
                ('content', models.TextField(help_text='One command per line', verbose_name='Content')),
                ('ignore_case', models.BooleanField(default=True, verbose_name='Ignore case')),
            ],
            options={
                'verbose_name': 'Command group',
            },
        ),
        migrations.CreateModel(
            name='ConnectMethodACL',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('priority', models.IntegerField(default=50, help_text='1-100, the lower the value will be match first', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Priority')),
                ('action', models.CharField(default='reject', max_length=64, verbose_name='Action')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('users', common.db.fields.JSONManyToManyField(default=dict, to='users.User', verbose_name='Users')),
                ('connect_methods', models.JSONField(default=list, verbose_name='Connect methods')),
            ],
            options={
                'verbose_name': 'Connect method acl',
                'ordering': ('priority', '-is_active', 'name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoginACL',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('priority', models.IntegerField(default=50, help_text='1-100, the lower the value will be match first', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Priority')),
                ('action', models.CharField(default='reject', max_length=64, verbose_name='Action')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('users', common.db.fields.JSONManyToManyField(default=dict, to='users.User', verbose_name='Users')),
                ('rules', models.JSONField(default=dict, verbose_name='Rule')),
            ],
            options={
                'verbose_name': 'Login acl',
                'ordering': ('priority', '-is_active', 'name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoginAssetACL',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('priority', models.IntegerField(default=50, help_text='1-100, the lower the value will be match first', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Priority')),
                ('action', models.CharField(default='reject', max_length=64, verbose_name='Action')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('users', common.db.fields.JSONManyToManyField(default=dict, to='users.User', verbose_name='Users')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('assets', common.db.fields.JSONManyToManyField(default=dict, to='assets.Asset', verbose_name='Assets')),
                ('accounts', models.JSONField(default=list, verbose_name='Accounts')),
                ('rules', models.JSONField(default=dict, verbose_name='Rule')),
            ],
            options={
                'verbose_name': 'Login asset acl',
                'ordering': ('priority', '-is_active', 'name'),
                'abstract': False,
            },
        ),
    ]
