# Generated by Django 2.1.4 on 2019-04-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0007_auto_20190413_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]