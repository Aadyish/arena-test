# Generated by Django 5.1.4 on 2024-12-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena_app', '0006_alter_booking_sessionid_alter_booking_userid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='sessions',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
