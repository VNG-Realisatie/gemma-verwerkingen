# Generated by Django 2.0.3 on 2018-03-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20180308_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='vergunningsaanvraag',
            name='lokatie_plaats',
            field=models.CharField(default='Haarlem', max_length=100),
            preserve_default=False,
        ),
    ]
