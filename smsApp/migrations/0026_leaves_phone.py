# Generated by Django 4.2.2 on 2023-07-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0025_leaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaves',
            name='phone',
            field=models.CharField(default=1, max_length=11, verbose_name='手机号'),
            preserve_default=False,
        ),
    ]
