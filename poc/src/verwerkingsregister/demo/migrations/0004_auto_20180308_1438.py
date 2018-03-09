# Generated by Django 2.0.3 on 2018-03-08 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_vergunningsaanvraag_lokatie_plaats'),
    ]

    operations = [
        migrations.AddField(
            model_name='vergunningsaanvraag',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vergunningsaanvraag',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]