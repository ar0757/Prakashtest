# Generated by Django 3.2.19 on 2023-06-19 07:33

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0004_remove_volunteer_profiles_volunteer_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
