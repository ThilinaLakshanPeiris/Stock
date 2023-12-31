# Generated by Django 4.1.2 on 2023-08-02 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='region',
            fields=[
                ('region_txt', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('region_id', models.IntegerField(primary_key=True, serialize=False)),
                ('region_code', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('priority', models.IntegerField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_level',
            fields=[
                ('level_id', models.AutoField(primary_key=True, serialize=False)),
                ('level_name', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('status', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_id_set', serialize=False, to='stc.users')),
                ('first_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('created_time', models.TimeField(blank=True, default=None, max_length=100, null=True)),
                ('image_url', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('tel_no', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='region_auth',
            fields=[
                ('region_auth_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_id', models.IntegerField(blank=True, default=None, null=True)),
                ('deport_id', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user_level', models.IntegerField(blank=True, default=None, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reg_id_set', to='stc.users')),
            ],
        ),
        migrations.CreateModel(
            name='depot',
            fields=[
                ('depot_id', models.AutoField(primary_key=True, serialize=False)),
                ('depot_txt', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('deport_tel', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('deport_image', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('priority', models.BooleanField(default=True)),
                ('sortid', models.BooleanField(default=True)),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_region_set', to='stc.region')),
            ],
        ),
    ]
