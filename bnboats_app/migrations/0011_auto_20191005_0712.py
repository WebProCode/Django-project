# Generated by Django 2.1.7 on 2019-10-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnboats_app', '0010_userprofile_fishing_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]