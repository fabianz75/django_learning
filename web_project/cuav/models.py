# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Classification(models.Model):
    classification_type = models.TextField(blank=True, null=True)
    drone_comm_type = models.TextField(blank=True, null=True)
    matching_drone_ids = models.TextField(blank=True, null=True)

    
    class Meta:
        db_table = 'classification'


class Drone(models.Model):
    drone_type = models.ForeignKey('DroneType', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    manufacture_id = models.TextField(blank=True, null=True)
    rac_unique_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'drone'


class DroneFlight(models.Model):
    test_case = models.ForeignKey('TestCase', models.DO_NOTHING, blank=True, null=True)
    drone_flight_id = models.IntegerField(blank=True, null=True)
    drone = models.ForeignKey(Drone, models.DO_NOTHING, blank=True, null=True)
    datetime_utc = models.DateTimeField(blank=True, null=True)
    latitude_wgs84 = models.FloatField(blank=True, null=True)
    longitude_wgs84 = models.FloatField(blank=True, null=True)
    elevation_m = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'drone_flight'


class DroneType(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'drone_type'


class MeasuringDevice(models.Model):
    measuring_device_type = models.ForeignKey('MeasuringDeviceType', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, blank=True, null=True)
    manufacture_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'measuring_device'


class MeasuringDeviceType(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'measuring_device_type'


class SystemStatus(models.Model):
    test_case = models.ForeignKey('TestCase', models.DO_NOTHING, blank=True, null=True)
    measuring_device = models.ForeignKey(MeasuringDevice, models.DO_NOTHING, blank=True, null=True)
    sensor_id = models.TextField(blank=True, null=True)
    datetime_utc = models.DateTimeField(blank=True, null=True)
    position_latitude_wgs84 = models.FloatField(blank=True, null=True)
    position_longitude_wgs84 = models.FloatField(blank=True, null=True)
    position_altitude_wgs84 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'system_status'


class TargetMeasurement(models.Model):
    test_case = models.ForeignKey('TestCase', models.DO_NOTHING, blank=True, null=True)
    measuring_device = models.ForeignKey(MeasuringDevice, models.DO_NOTHING, blank=True, null=True)
    track_id = models.IntegerField(blank=True, null=True)
    sensor_id = models.TextField(blank=True, null=True)
    datetime_utc = models.DateTimeField(blank=True, null=True)
    target_distance_m = models.FloatField(blank=True, null=True)
    target_latitude_wgs84 = models.FloatField(blank=True, null=True)
    target_longitude_wgs84 = models.FloatField(blank=True, null=True)
    target_altitude_wgs84 = models.FloatField(blank=True, null=True)
    target_azimuth_deg = models.FloatField(blank=True, null=True)
    target_classification_type = models.TextField(blank=True, null=True)
    target_communication_type = models.TextField(blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'target_measurement'


class TestCase(models.Model):
    datetime_utc = models.DateTimeField(blank=True, null=True)
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    location = models.TextField()

    class Meta:
        db_table = 'test_case'


class TestScenario(models.Model):
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING, blank=True, null=True)
    start_time_utc = models.DateTimeField(blank=True, null=True)
    end_time_utc = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'test_scenario'


class Track(models.Model):
    track_id = models.IntegerField(blank=True, null=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING, blank=True, null=True)
    measuring_device = models.ForeignKey(MeasuringDevice, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'track'


class Vendor(models.Model):
    name = models.TextField()
    class Meta:
        db_table = 'vendor'
