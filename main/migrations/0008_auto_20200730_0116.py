# Generated by Django 3.0.8 on 2020-07-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200730_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(max_length=200),
        ),
    ]
