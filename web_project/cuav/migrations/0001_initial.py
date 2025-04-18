# Generated by Django 5.2 on 2025-04-09 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification_type', models.TextField(blank=True, null=True)),
                ('drone_comm_type', models.TextField(blank=True, null=True)),
                ('matching_drone_ids', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'classification',
            },
        ),
        migrations.CreateModel(
            name='DroneType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'drone_type',
            },
        ),
        migrations.CreateModel(
            name='MeasuringDeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'measuring_device_type',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_utc', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('location', models.TextField()),
            ],
            options={
                'db_table': 'test_case',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('manufacture_id', models.TextField(blank=True, null=True)),
                ('rac_unique_id', models.TextField(blank=True, null=True)),
                ('drone_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.dronetype')),
            ],
            options={
                'db_table': 'drone',
            },
        ),
        migrations.CreateModel(
            name='MeasuringDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('manufacture_id', models.TextField(blank=True, null=True)),
                ('measuring_device_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.measuringdevicetype')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.vendor')),
            ],
            options={
                'db_table': 'measuring_device',
            },
        ),
        migrations.CreateModel(
            name='TargetMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.IntegerField(blank=True, null=True)),
                ('sensor_id', models.TextField(blank=True, null=True)),
                ('datetime_utc', models.DateTimeField(blank=True, null=True)),
                ('target_distance_m', models.FloatField(blank=True, null=True)),
                ('target_latitude_wgs84', models.FloatField(blank=True, null=True)),
                ('target_longitude_wgs84', models.FloatField(blank=True, null=True)),
                ('target_altitude_wgs84', models.FloatField(blank=True, null=True)),
                ('target_azimuth_deg', models.FloatField(blank=True, null=True)),
                ('target_classification_type', models.TextField(blank=True, null=True)),
                ('target_communication_type', models.TextField(blank=True, null=True)),
                ('confidence', models.FloatField(blank=True, null=True)),
                ('measuring_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.measuringdevice')),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.testcase')),
            ],
            options={
                'db_table': 'target_measurement',
            },
        ),
        migrations.CreateModel(
            name='SystemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.TextField(blank=True, null=True)),
                ('datetime_utc', models.DateTimeField(blank=True, null=True)),
                ('position_latitude_wgs84', models.FloatField(blank=True, null=True)),
                ('position_longitude_wgs84', models.FloatField(blank=True, null=True)),
                ('position_altitude_wgs84', models.FloatField(blank=True, null=True)),
                ('measuring_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.measuringdevice')),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.testcase')),
            ],
            options={
                'db_table': 'system_status',
            },
        ),
        migrations.CreateModel(
            name='DroneFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_flight_id', models.IntegerField(blank=True, null=True)),
                ('datetime_utc', models.DateTimeField(blank=True, null=True)),
                ('latitude_wgs84', models.FloatField(blank=True, null=True)),
                ('longitude_wgs84', models.FloatField(blank=True, null=True)),
                ('elevation_m', models.FloatField(blank=True, null=True)),
                ('drone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.drone')),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.testcase')),
            ],
            options={
                'db_table': 'drone_flight',
            },
        ),
        migrations.CreateModel(
            name='TestScenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time_utc', models.DateTimeField(blank=True, null=True)),
                ('end_time_utc', models.DateTimeField(blank=True, null=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.testcase')),
            ],
            options={
                'db_table': 'test_scenario',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.IntegerField(blank=True, null=True)),
                ('measuring_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.measuringdevice')),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.testcase')),
            ],
            options={
                'db_table': 'track',
            },
        ),
        migrations.AddField(
            model_name='testcase',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuav.vendor'),
        ),
    ]
