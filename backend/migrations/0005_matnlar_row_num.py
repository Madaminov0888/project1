# Generated by Django 3.2.8 on 2022-09-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20220919_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='matnlar',
            name='row_num',
            field=models.IntegerField(default=3, null=True),
        ),
    ]