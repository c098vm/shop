# Generated by Django 4.2.4 on 2023-08-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='create_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]
