# Generated by Django 2.2.2 on 2019-07-24 14:54

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', django_resized.forms.ResizedImageField(crop=None, force_format=('JPEG', 'PNG'), keep_meta=True, quality=100, size=[1920, 1080], upload_to='schedule/')),
            ],
        ),
    ]
