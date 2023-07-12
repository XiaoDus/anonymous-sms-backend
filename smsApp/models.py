from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator  # 限制IntegerField的取值范围


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name='昵称', max_length=8)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    url=models.CharField(verbose_name='头像URL',max_length=999)
    session_key=models.CharField(verbose_name='session_key',max_length=999)
    openId=models.CharField(verbose_name='openId',max_length=999)
    successCount=models.IntegerField(verbose_name='成功条数',validators=[MinValueValidator(0)], default=0)
    failCount=models.IntegerField(verbose_name='失败条数',validators=[MinValueValidator(0)], default=0)
    replyCount=models.IntegerField(verbose_name='回复条数',validators=[MinValueValidator(0)], default=0)



class successMail(models.Model):
    uid=models.CharField(verbose_name='订单号',max_length=11)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    forPhone=models.CharField(verbose_name='对方手机号',max_length=11)
    mail = models.CharField(verbose_name='成功短信', max_length=800)
    isOpenChoice = (
        (1, 'true'),
        (0, 'false')
    )
    isOpen = models.SmallIntegerField(choices=isOpenChoice, default=0,verbose_name='是否公开')
    sendTime=models.CharField(verbose_name='发送时间' ,max_length=20)
    nickName=models.CharField(verbose_name='昵称', max_length=8)
    imgUrl=models.CharField(verbose_name='头像地址',max_length=999)
    class Meta:
        ordering = ['-sendTime'] # 以后进行提取数据时，按照指定字段的排序提取数据


class failMail(models.Model):
    uid=models.CharField(verbose_name='uid',max_length=11)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    forPhone=models.CharField(verbose_name='对方手机号',max_length=11)
    mail = models.CharField(verbose_name='异常短信', max_length=800)
    isOpenChoice = (
        (1, 'true'),
        (0, 'false')
    )
    isOpen = models.SmallIntegerField(choices=isOpenChoice, default=0, verbose_name='是否公开')
    sendTime=models.CharField(verbose_name='发送时间' ,max_length=20)
    nickName=models.CharField(verbose_name='昵称', max_length=8)

    class Meta:
        ordering = ['-sendTime']

class leaves(models.Model):
    forName=models.CharField(verbose_name='对方名称',max_length=99)
    nickName=models.CharField(verbose_name='昵称', max_length=8,default='匿名用户')
    imgUrl=models.CharField(verbose_name='头像地址',max_length=999,default='https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/0.png')
    sendTime=models.CharField(verbose_name='发送时间' ,max_length=20)
    mail = models.CharField(verbose_name='留言', max_length=800)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    uid=models.CharField(verbose_name='订单号',max_length=11)




class replyMail(models.Model):
    uid=models.CharField(verbose_name='uid',max_length=11)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    forPhone=models.CharField(verbose_name='对方手机号',max_length=11)
    mail = models.CharField(verbose_name='我的回复', max_length=800)
    myMail = models.CharField(verbose_name='我的短信', max_length=800)
    sendTime=models.CharField(verbose_name='发送时间' ,max_length=20)

class labour(models.Model):
    uid = models.CharField(verbose_name='uid', max_length=11)
    wayChoice = (
        (1, '微信'),
        (2, 'QQ'),
        (3, '抖音'),
        (4, '快手'),
        (5, '微博'),
        (6, '小红书')
    )
    way=models.SmallIntegerField(choices=wayChoice,verbose_name='联系方式',default=0)
    phone = models.CharField(verbose_name='用户手机号', max_length=11)
    forPhone = models.CharField(verbose_name='对方账号', max_length=11)
    mail = models.CharField(verbose_name='短信内容', max_length=9999)
    isOpenChoice = (
        (1, 'true'),
        (0, 'false')
    )
    isOpen = models.SmallIntegerField(choices=isOpenChoice, default=0, verbose_name='是否公开')
    sendTime = models.CharField(verbose_name='发送时间', max_length=20)
    nickName = models.CharField(verbose_name='昵称', max_length=8)
    sendTime = models.CharField(verbose_name='发送时间', max_length=20)
    nickName = models.CharField(verbose_name='昵称', max_length=8)
    imgUrl = models.CharField(verbose_name='头像地址', max_length=999)
    isSendChoice = (
        (1, 'true'),
        (0, 'false')
    )
    isSend= models.SmallIntegerField(choices=isSendChoice,verbose_name='是否发送',default=0)



