# Generated by Django 4.2.2 on 2023-07-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0008_remove_failmail_uid_remove_replymail_uid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='openId',
            field=models.CharField(default=1, max_length=999, verbose_name='openId'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='session_key',
            field=models.CharField(default=1, max_length=999, verbose_name='session_key'),
            preserve_default=False,
        ),
    ]
