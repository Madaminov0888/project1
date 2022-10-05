# Generated by Django 3.2.8 on 2022-09-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_matnlar_buttons'),
    ]

    operations = [
        migrations.AddField(
            model_name='botusers',
            name='situation',
            field=models.CharField(default='-', max_length=33, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='situation',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='matnlar',
            name='buttons',
            field=models.ManyToManyField(to='backend.Buttons'),
        ),
    ]
