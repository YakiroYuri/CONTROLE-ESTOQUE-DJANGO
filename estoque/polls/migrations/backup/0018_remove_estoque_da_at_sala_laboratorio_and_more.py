# Generated by Django 5.0.3 on 2024-03-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_alter_estoque_sala_laboratorio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque_da_at',
            name='sala_laboratorio',
        ),
        migrations.RemoveField(
            model_name='historicalestoque_da_at',
            name='sala_laboratorio',
        ),
        migrations.AlterField(
            model_name='estoque',
            name='sala_laboratorio',
            field=models.CharField(blank=True, choices=[('sala1', 'Sala 1'), ('sala2', 'Sala 2'), ('sala3', 'Sala 3')], max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalestoque',
            name='sala_laboratorio',
            field=models.CharField(blank=True, choices=[('sala1', 'Sala 1'), ('sala2', 'Sala 2'), ('sala3', 'Sala 3')], max_length=100),
        ),
    ]
