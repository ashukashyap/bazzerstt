# Generated by Django 3.0.4 on 2021-03-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210219_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='gali',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
