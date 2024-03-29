# Generated by Django 5.0.3 on 2024-03-20 19:59

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('service_type', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('agency_name', models.CharField(max_length=200, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_be_contacted', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='agencies.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
