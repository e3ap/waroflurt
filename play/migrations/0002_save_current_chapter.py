# Generated by Django 2.2 on 2019-05-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='save',
            name='current_chapter',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
