# Generated by Django 2.2.2 on 2019-07-28 15:39

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, size=[1920, 1080], upload_to='schedule/'),
        ),
    ]
