"""
URL configuration for smsTool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smsApp import views
urlpatterns = [
    path('MailCount/', views.MailCount), #短信条数
    path('getSessionKey/', views.getSessionKey), #获取用户信息
    path('getMailMessage/', views.getMailMessage), #获取短信信息
    path('saveMailMessage/', views.saveMailMessage), #保存发送短信
    path('mailReply/', views.mailReply), #回复短信短信
    path('openMailMessage/', views.openMailMessage), #公开短信
    path('get_prepay_order/', views.get_prepay_order), #获取支付预订单
    path('notify/', views.notify), #支付成功通知地址
    path('decrypt/', views.decrypt), #解码获取手机号
    path('labour/', views.labour), #人工传话
    path('getLabour/', views.getLabour), #获取人工传话信息
    path('leaves/', views.leaves), #留言板

]
