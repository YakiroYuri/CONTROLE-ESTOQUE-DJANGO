# Generated by Django 5.0.3 on 2024-03-19 15:17

import django.db.models.deletion
import django.utils.timezone
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('retirada', models.IntegerField(default=0)),
                ('estoque', models.IntegerField()),
                ('data_estoque', models.DateTimeField(default=django.utils.timezone.now)),
                ('sala_laboratorio', models.CharField(blank=True, choices=[('a', 'd'), ('b', 'e'), ('c', 'f')])),
            ],
        ),
        migrations.CreateModel(
            name='Estoque_da_at',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('retirada', models.IntegerField(default=0)),
                ('estoque', models.IntegerField()),
                ('data_estoque', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalEstoque',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('nome', models.CharField(max_length=50)),
                ('retirada', models.IntegerField(default=0)),
                ('estoque', models.IntegerField()),
                ('data_estoque', models.DateTimeField(default=django.utils.timezone.now)),
                ('sala_laboratorio', models.CharField(blank=True, choices=[('a', 'd'), ('b', 'e'), ('c', 'f')])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical estoque',
                'verbose_name_plural': 'historical estoques',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEstoque_da_at',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('nome', models.CharField(max_length=50)),
                ('retirada', models.IntegerField(default=0)),
                ('estoque', models.IntegerField()),
                ('data_estoque', models.DateTimeField(default=django.utils.timezone.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical estoque_da_at',
                'verbose_name_plural': 'historical estoque_da_ats',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
