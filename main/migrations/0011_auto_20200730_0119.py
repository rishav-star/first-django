# Generated by Django 3.0.8 on 2020-07-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200730_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
