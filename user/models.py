from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('账号',max_length=30)
    password = models.CharField('密码',max_length=32)
    phone = models.CharField('手机号',max_length=32)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    email = models.EmailField('邮箱',max_length=32,default=None)
    #是否入职（默认0 未入职，1 入职）
    is_induction = models.IntegerField('是否入职',default=0)
    #是否激活(默认0 未激活,1 激活)
    #isActive = models.IntegerField('是否激活',default=0)

    def __str__(self):

        return '用户名:%s'%self.username

class IpInfo(models.Model):
    uname = models.CharField('用户',max_length=30)
    ip_adress = models.CharField('ip地址',max_length=50)
    login_time = models.DateTimeField('登录时间',auto_now_add=True)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    clock_time = models.DateTimeField('被锁时间',auto_now=True)
    # 是否加锁 1是没有被锁
    isAticv = models.IntegerField('是否被激活',default=1)

