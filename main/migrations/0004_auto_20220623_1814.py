# Generated by Django 2.1.3 on 2022-06-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220623_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindata',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
    ]