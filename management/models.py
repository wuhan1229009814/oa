# Create your models here.

from django.db import models



# 员工表
from department.models import Position, Department
from user.models import User


class Management(models.Model):
    id = models.AutoField('id', primary_key=True)
    job_no = models.CharField('工号',max_length=16,null=True,default='')
    dep_name = models.CharField('部门名称',max_length=16,null=True,default='')
    position_name = models.CharField('部门职位',max_length=16,null=True,default='')
    sex = models.CharField('男',max_length=2,null=True,default='')
    power = models.CharField('权限',max_length=2,null=True,default='')
    name = models.CharField('姓名',max_length=30,null=True,default='')
    username = models.CharField('账号',max_length=30)
    phone = models.CharField('手机号',max_length=32)
    img = models.CharField('图片路径',max_length=64,default='')
    create_time = models.DateTimeField('入职时间',null=True,default=None)
    email = models.EmailField('邮箱',max_length=32,default=None)
    department = models.ForeignKey(Department,null=True,default=None)
    position = models.ForeignKey(Position,null=True,default=None)
    user = models.OneToOneField(User,null=True,default=None)
    def __str__(self):

        return '用户名:%s'%self.job_no