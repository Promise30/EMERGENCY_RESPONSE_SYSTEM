# Generated by Django 5.0.3 on 2024-03-19 23:47

import django.db.models.deletion
import emergency_response_system.utils.constants
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[(emergency_response_system.utils.constants.EmergencyReportStatus['UNRESOLVED'], 'Unresolved'), (emergency_response_system.utils.constants.EmergencyReportStatus['IN_PROGRESS'], 'In progress'), (emergency_response_system.utils.constants.EmergencyReportStatus['RESOLVED'], 'Resolved')], default=emergency_response_system.utils.constants.EmergencyReportStatus['UNRESOLVED'], max_length=10)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencies.agency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
