# Generated by Django 5.0.7 on 2024-08-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Best blog Site', max_length=255),
        ),
    ]
