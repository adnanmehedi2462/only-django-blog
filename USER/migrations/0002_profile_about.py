# Generated by Django 4.0.5 on 2022-06-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]