# Generated by Django 2.2 on 2019-04-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BooksAdmin', '0003_auto_20190427_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='parent_chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BooksAdmin.Chapter'),
        ),
    ]