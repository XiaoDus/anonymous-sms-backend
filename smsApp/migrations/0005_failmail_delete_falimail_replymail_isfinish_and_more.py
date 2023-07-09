# Generated by Django 4.2.2 on 2023-06-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0004_falimail_replymail_successmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='failMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=8, verbose_name='ID')),
                ('fail', models.CharField(max_length=800, verbose_name='异常短信')),
                ('isFinish', models.SmallIntegerField(choices=[(1, 'true'), (2, 'false')], default=2, verbose_name='是否公开')),
            ],
        ),
        migrations.DeleteModel(
            name='faliMail',
        ),
        migrations.AddField(
            model_name='replymail',
            name='isFinish',
            field=models.SmallIntegerField(choices=[(1, 'true'), (2, 'false')], default=2, verbose_name='是否公开'),
        ),
        migrations.AddField(
            model_name='successmail',
            name='isFinish',
            field=models.SmallIntegerField(choices=[(1, 'true'), (2, 'false')], default=2, verbose_name='是否公开'),
        ),
    ]
