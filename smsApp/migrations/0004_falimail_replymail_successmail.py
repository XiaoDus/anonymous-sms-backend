# Generated by Django 4.2.2 on 2023-06-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0003_userinfo_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='faliMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=8, verbose_name='ID')),
                ('fali', models.CharField(max_length=800, verbose_name='异常短信')),
            ],
        ),
        migrations.CreateModel(
            name='replyMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=8, verbose_name='ID')),
                ('reply', models.CharField(max_length=800, verbose_name='我的回复')),
            ],
        ),
        migrations.CreateModel(
            name='successMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=8, verbose_name='ID')),
                ('mail', models.CharField(max_length=800, verbose_name='成功短信')),
            ],
        ),
    ]
