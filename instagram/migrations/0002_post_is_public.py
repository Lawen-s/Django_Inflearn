# Generated by Django 3.0.14 on 2022-07-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='공개여부'),
        ),
    ]
