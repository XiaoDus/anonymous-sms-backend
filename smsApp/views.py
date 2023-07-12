# -- coding: utf-8 --**
#-*-coding:utf-8-*-
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import random
import string
from smsApp import models
from smsApp.static.sms import sendSMS
import json
from smsApp.static.WXBizDataCrypt import WXBizDataCrypt

def UserLogin(name, phone, url, key, openId):
    '''登陆注册用户'''
    # 判断数据库中是否有用该用户
    if not models.UserInfo.objects.filter(phone=phone).exists():  # 如果没有则创建
        models.UserInfo.objects.create(name=name, phone=phone, url=url, session_key=key, openId=openId)
    else:
        models.UserInfo.objects.filter(phone=phone).update(session_key=key,
                                                           openId=openId)  # 否则就更新信息


@csrf_exempt
def getSessionKey(request):
    '''获取用户信息'''
    if request.method == 'POST':
        # 前端发送的信息
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        unicode = json_data['code']  # 前端发送的code
        name = json_data['name']  # 昵称
        aurl = json_data['url']  # 头像地址
        encryptedData = json_data['encryptedData']
        iv = json_data['iv']
        msg = {
            'appid': 'wx721656e2f1d02e7d',  # 微信小程序appid
            'secret': '540982264045c098a0cf72872a4a8ab9',  # 微信小程序appsecret
            'js_code': unicode,  # 前端用uni.login({OBJECT})获取的code
            'grant_type': 'authorization_code'
        }

        # 请求微信服务器用code获取sessionKey,openId
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx721656e2f1d02e7d&secret=540982264045c098a0cf72872a4a8ab9&grant_type=authorization_code&js_code=' + unicode
        response = requests.get(url)
        # 处理响应数据
        json_data1 = response.json()
        if json_data1:
            # 加密
            key = json_data1['session_key']
            openId = json_data1['openid']
            phoneNumber = decrypt(encryptedData, iv, key)  # 解码获取电话
            if(phoneNumber):
                UserLogin(name, phoneNumber, aurl, key, openId) # 注册
                # 返回响应结果
                return JsonResponse({'phoneNumber': phoneNumber})
            return JsonResponse({'phoneNumber': ''})




import base64
import json
from Crypto.Cipher import AES
# 解码获取手机号
def decrypt(encryptedData, iv, session_key):
    '''微信信息解码'''
    app_id = 'wx721656e2f1d02e7d'
    i=1
    while i<99:
        try:
            # 使用 session_key 和 iv 创建一个解密器
            crypt = WXBizDataCrypt(app_id, session_key)
            # 对加密数据进行解密
            decrypted_data = crypt.decrypt(encryptedData, iv)
            # print(decrypted_data['phoneNumber'])
            return decrypted_data['phoneNumber']
        except:
            i+=1






@csrf_exempt
def MailCount(request):
    '''短信条数'''
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        phone = json_data['phone']
        if phone:
            '''
            判断号码是否为空
            并获取该号码短信数量
            '''
            getSuccessCount = models.successMail.objects.filter(phone=phone).count()
            getfailCount = models.failMail.objects.filter(phone=phone).count()
            getreplyCount = models.replyMail.objects.filter(phone=phone).count()
            models.UserInfo.objects.filter(phone=phone).update(successCount=getSuccessCount, failCount=getfailCount,
                                                               replyCount=getreplyCount)
            result = {
                'successCount': getSuccessCount,
                'failCount': getfailCount,
                'replyCount': getreplyCount
            }
            return JsonResponse(result)
        result = {
            'successCount': 0,
            'failCount': 0,
            'replyCount': 0
        }
        return JsonResponse(result)


@csrf_exempt
def getMailMessage(request):
    if request.method == 'POST':
        '''获取短信信息'''
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        phone = json_data['phone']

        getSuccessList = models.successMail.objects.filter(phone=phone).all().values()
        getFailList = models.failMail.objects.filter(phone=phone).all().values()
        getReplyList = models.replyMail.objects.filter(phone=phone).all().values()
        if not getSuccessList:  # 判断是否为空值
            getSuccessList = []
        else:
            successList = []
            for i in getSuccessList:
                successList.append(i)
            getSuccessList = successList[:]

        if not getFailList:
            getFailList = []
        else:
            failList = []
            for i in getFailList:
                failList.append(i)
            getFailList = failList[:]

        if not getReplyList:
            getReplyList = []
        else:
            replyList = []
            for i in getReplyList:
                replyList.append(i)
            getReplyList = replyList[:]

        result = {
            'successMail': getSuccessList,
            'failMail': getFailList,
            'replyMail': getReplyList
        }
        return JsonResponse(result)
    elif request.method == 'GET':
        '''更改短信是否公开'''
        uid = request.GET.get('uid')
        listName = request.GET.get('listName')
        isOpen = request.GET.get('isOpen')
        if listName == 'success':
            models.successMail.objects.filter(uid=uid).update(isOpen=isOpen)
            return JsonResponse({'isOpen': isOpen})
        elif listName == 'reply':
            models.replyMail.objects.filter(uid=uid).update(isOpen=isOpen)
            return JsonResponse({'isOpen': isOpen})


@csrf_exempt
def saveMailMessage(request):
    '''保存发送的短信'''
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        userPhone = json_data['userPhone']
        forPhone = json_data['forPhone']
        isOpen = json_data['isOpen']
        nickName = json_data['nickName']
        mailText = json_data['mailText']
        avatarUrl = json_data['avatarUrl']
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        uid = json_data['out_trade_no']  # 订单号
        result = sendSMS(forPhone, mailText)
        if result == '200':
            if models.UserInfo.objects.filter(phone=userPhone).exists():
                models.successMail.objects.create(imgUrl=avatarUrl, nickName=nickName, phone=userPhone,
                                                  forPhone=forPhone,
                                                  uid=uid, isOpen=isOpen, mail=mailText,
                                                  sendTime=nowTime)
                rueslt = {
                    'static': 200
                }
                return JsonResponse(rueslt)
            return JsonResponse({'static': 500})

from django.http import HttpResponse
@csrf_exempt
def mailReply(request):
    '''短信回复'''
    if request.method == 'POST':
        '''获取短信信息'''
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        print(json_data)
        if not json_data[0]['report_status'] == 'SUCCESS': #短信发送成功的回调
            pass
        forPhone=json_data['mobile'] #回复的手机号
        text=json_data['text'] #内容
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        while True:
            a=0
            b=1
            getMail=models.successMail.objects.order_by('-id')[a:b].values()[0]
            if getMail['forPhone'] == forPhone:
                models.replyMail.objects.create(phone=getMail['phone'],forPhone=forPhone,uid=getMail['uid'],mail=text,myMail=getMail['mail'],sendTime=nowTime)
                break
            a+=1
            b+=1
        return JsonResponse({'code':200})
@csrf_exempt
def openMailMessage(request):
    '''公开信息'''
    if request.method == 'GET':
        mailMessage = []
        getMailList = models.successMail.objects.filter(isOpen=1).all().values().order_by('?')
        getLabour=models.labour.objects.filter(isOpen=1).all().values().order_by('?')
        if not getMailList:
            getMailList = []
        else:
            for i in getMailList:
                mailMessage.append(i)
        if not getLabour:
            getLabour = []
        else:
            for i in getLabour:
                mailMessage.append(i)

        result = {
            'data': mailMessage
        }
        return JsonResponse(result)


@csrf_exempt
def leaves(request):
    if request.method == 'GET':
        mailMessage = []
        forName=request.GET.get('forName')
        getMailList = models.leaves.objects.filter(forName=forName).all().values().order_by('?')
        if not getMailList:
            getMailList = []
        else:
            for i in getMailList:
                mailMessage.append(i)

        result = {
            'data': mailMessage
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        userPhone = json_data['userPhone']
        forName = json_data['forName']
        nickName = json_data['nickName']
        mailText = json_data['mailText']
        avatarUrl = json_data['avatarUrl']
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        uid = json_data['out_trade_no']  # 订单号
        models.leaves.objects.create(uid=uid,imgUrl=avatarUrl, nickName=nickName, phone=userPhone,forName=forName, mail=mailText,
                                     sendTime=nowTime)
        rueslt = {
            'static': 200
        }
        return JsonResponse(rueslt)



# 微信支付信息订单
import hashlib
import random
import requests
import xml.etree.ElementTree as ET


# 定义一个生成随机字符串的函数
def generate_nonce_str(length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for i in range(length))


# 定义一个生成签名的函数
def generate_sign(params, key):
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    string_a = '&'.join(f'{key}={value}' for key, value in sorted_params)
    string_sign_temp = f'{string_a}&key={key}'
    md5 = hashlib.md5()
    md5.update(string_sign_temp.encode('utf-8','ignore'))
    print('sginkey:', md5.hexdigest().upper())
    return md5.hexdigest().upper()


# 定义一个获取预支付订单的函数
import time


@csrf_exempt
def get_prepay_order(request):


    data = request.body
    params = json.loads(data)
    userPhone = params['userPhone']
    openID = models.UserInfo.objects.filter(phone=userPhone).values('openId')[0]['openId']
    # 构造请求参数
    appid = 'wx721656e2f1d02e7d'  # 小程序 AppID
    mch_id = '1648295608'  # 商户号
    nonce_str = generate_nonce_str(16)  # 随机字符串
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip:
        spbill_create_ip=ip
    else:
        spbill_create_ip = params['ip']  # 用户使用的设备的 IP
    body = params['body']  # 商品描述
    out_trade_no = params['out_trade_no']  # 商户订单号
    total_fee = params['total_fee']  # 订单总金额，单位为分
    notify_url = 'https://1el9898253.oicp.vip/notify/'  # 支付结果通知地址 POST请求
    trade_type = 'JSAPI'  # 交易类型，此处固定为 JSAPI
    openid = openID  # 用户的 openid，从前端小程序获取
    current_time = str(int(time.time()))
    # 构造签名
    sign_params = {
        'appid': appid,
        'mch_id': mch_id,
        'nonce_str': nonce_str,
        'body': body,
        'out_trade_no': out_trade_no,
        'total_fee': total_fee,
        'spbill_create_ip': spbill_create_ip,
        'notify_url': notify_url,
        'trade_type': trade_type,
        'openid': openid,
    }
    print(sign_params)

    sign = generate_sign(sign_params, 'duxinghai826012560duxinghai04950')  # 商户密钥
    # 构造 XML 格式的请求体
    request_body = f'''
        <xml>
            <appid>{appid}</appid>
             <body>{body}</body>
            <mch_id>{mch_id}</mch_id>
            <nonce_str>{nonce_str}</nonce_str>
            <notify_url>{notify_url}</notify_url>
            <openid>{openid}</openid>
            <out_trade_no>{out_trade_no}</out_trade_no>
            <spbill_create_ip>{spbill_create_ip}</spbill_create_ip>
            <total_fee>{total_fee}</total_fee>
            <trade_type>{trade_type}</trade_type>
            <sign>{sign}</sign>
        </xml>
    '''

    # 发送请求并解析响应结果
    # if (response_xml.find('prepay_id')):
    try:
        response = requests.post('https://api2.mch.weixin.qq.com/pay/unifiedorder', data=request_body.encode('utf-8','ignore'))
        response.encoding = 'utf-8'
        response_xml = ET.fromstring(response.text)
        prepay_id = response_xml.find('prepay_id').text
        print('prepay_id=', prepay_id)
        # 返回预支付订单 ID
    except:
        response = requests.post('https://api.mch.weixin.qq.com/pay/unifiedorder', data=request_body.encode('utf-8','ignore'))
        response.encoding = 'utf-8'
        response_xml = ET.fromstring(response.text)
        prepay_id = response_xml.find('prepay_id').text
    else:
        sign_key = {
            'appId': appid,
            'nonceStr': nonce_str,
            'package': 'prepay_id=' + prepay_id,
            'signType': 'MD5',
            'timeStamp': current_time,
        }
        getSignKey = generate_sign(sign_key, 'duxinghai826012560duxinghai04950')  # 商户密钥

        return JsonResponse(
            {'code': 200, 'static': prepay_id, 'sign': getSignKey, 'nonce_str': nonce_str, 'timeStamp': current_time})
    return JsonResponse({'code': 500})


@csrf_exempt
def notify(request):
    return JsonResponse({'code': 200})


@csrf_exempt
def labour(request):
    '''人工传话'''
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)  # 把 json 数据转换为字典
        userPhone = json_data['userPhone']
        forPhone = json_data['forPhone']
        isOpen = json_data['isOpen']
        nickName = json_data['nickName']
        mailText = json_data['mailText']
        avatarUrl = json_data['avatarUrl']
        sendWay = json_data['sendWay']
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        uid = json_data['out_trade_no']  # 订单号
        if models.UserInfo.objects.filter(phone=userPhone).exists():
            if models.labour.objects.filter(phone=userPhone).exists():
                models.labour.objects.filter(phone=userPhone).all().update(imgUrl=avatarUrl, nickName=nickName)
            models.labour.objects.create(imgUrl=avatarUrl, nickName=nickName, phone=userPhone, way=sendWay,
                                         forPhone=forPhone,
                                         uid=uid, isOpen=isOpen, mail=mailText,
                                         sendTime=nowTime)
            rueslt = {
                'static': 200
            }
            return JsonResponse(rueslt)

@csrf_exempt
def getLabour(request):
    if request.method =='POST':
        labourList=models.labour.objects.filter(isSend=0).all().values()
        if not labourList:  # 判断是否为空值
            getLabourList = []
        else:
            List = []
            for i in labourList:
                List.append(i)
            getLabourList = List[:]

        return JsonResponse({'data':getLabourList})
    elif request.method =="GET":
        uid=request.GET.get('data')
        models.labour.objects.filter(uid=uid).update(isSend=1)
        return JsonResponse({'data':200})
