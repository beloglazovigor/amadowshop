# Generated by Django 2.1.7 on 2019-03-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20190318_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='send_mode',
            field=models.BooleanField(default=True),
        ),
    ]
