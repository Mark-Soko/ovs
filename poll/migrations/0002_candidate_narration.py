# Generated by Django 3.2.6 on 2021-09-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='narration',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]