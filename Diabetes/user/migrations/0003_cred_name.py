# Generated by Django 5.0.3 on 2024-04-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_cred_age_cred_height_cred_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='cred',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
