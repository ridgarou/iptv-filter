# Generated by Django 3.1.4 on 2020-12-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistChannel',
            fields=[
                ('id',           models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tvg_id',       models.CharField(max_length=50)),
                ('tvg_name',     models.CharField(db_index=True, max_length=100)),
                ('tvg_logo',     models.TextField()),
                ('group_title',  models.CharField(default='', max_length=50)),
                ('display_name', models.CharField(db_index=True, max_length=100)),
                ('stream_url',   models.URLField()),
                ('included',     models.BooleanField(db_index=True, default=None, null=True)),
                ('last_updated', models.DateTimeField(blank=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EpgChannel',
            fields=[
                ('id',           models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id',   models.CharField(db_index=True, max_length=50)),
                ('display_name', models.CharField(max_length=50)),
                ('icon',         models.TextField(null=True)),
                ('last_updated', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('included',     models.BooleanField(db_index=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppConfig',
            fields=[
                ('id',           models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key',          models.CharField(max_length=50)),
                ('value',        models.TextField(max_length=100)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CachedFile',
            fields=[
                ('id',           models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type',    models.TextField(max_length=5)),
                ('file',         models.BinaryField()),
                ('last_updated', models.DateTimeField(blank=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EpgProgramme',
            fields=[
                ('id',           models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start',        models.CharField(max_length=20)),
                ('stop',         models.CharField(max_length=20)),
                ('title',        models.CharField(max_length=100)),
                ('desc',         models.TextField(blank=True)),
                ('last_updated', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('channel',      models.CharField(db_index=True, max_length=50)),
                ('included',     models.BooleanField(db_index=True, default=None, null=True)),
            ],
        ),
    ]
