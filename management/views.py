"""部门管理模块"""
import datetime
import json
import os
import re
import time

from django.core import serializers
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from pymysql import DatabaseError

from common.Tools import getTimeStamp
from department.models import Department, Position
from management.models import Management
from user.models import User


def management_list(request):
    #获取用户名
    username = request.session.get("username")
    user = User.objects.filter(username = username)[0]
    management = Management.objects.filter(user = user)[0]
    #管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
    # 查询部门
    department_ids = Position.objects.values('department').distinct()
    position_list = Position.objects.all()
    ids = []
    for i in department_ids:
        ids.append(i['department'])
    department_list = Department.objects.filter(id__in=ids)

    if management.power == '1':
        power = '1'
        management_list = Management.objects.all().order_by('job_no')
    else:
        management_list = Management.objects.filter(~Q(job_no = '')).order_by('job_no')
    # 分页
    count = len(management_list)
    return render(request,'management/manager_info.html',locals())

def add_management(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        management = Management.objects.get(id=id)
        job_no = getTimeStamp()
        #只查询有职位的部门
        position_list = Position.objects.values('department').distinct()
        ids = []
        for i in position_list:
            ids.append(i['department'])
        department_list = Department.objects.filter(id__in = ids)

        return render(request,'management/management_add.html',locals())
    elif request.method == 'POST':
        myfile = None
        try:
            myfile = request.FILES['myfile']
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            file_path = os.path.join(os.path.join(BASE_DIR, 'static/files'), myfile.name)
            if myfile:
                with open(file_path, 'wb') as f:
                    data = myfile.file.read()
                    f.write(data)
        except Exception as e:
            print(e)
        #入职数据插入员工表
        id = request.POST.get('id')
        management = Management.objects.get(id = id)
        #获取前台数据
        #工号
        management_job_no = request.POST.get('job_no')
        management.job_no = management_job_no
        #部门
        dep_id = request.POST.get('dep_name')

        dep = Department.objects.get(id = dep_id)
        management.dep_name = dep.name
        #职位
        position_id = request.POST.get('position_name')
        position = Position.objects.get(id = position_id)
        management.position_id = position_id
        management.position_name = position.name
        #姓名
        management_name = request.POST.get('name')
        management.name = management_name
        #图片路径
        if myfile:
            management.img = '/static/files/'+myfile.name
        #性别
        sex = request.POST.get('sex')
        management.sex = sex
        #入职时间
        create_time = datetime.datetime.now()
        management.create_time = create_time
        #
        management.department_id = dep_id
        management.save()
        # 获取用户名
        username = request.session.get("username")
        user = User.objects.filter(username=username)[0]
        management = Management.objects.filter(user=user)[0]
        # 管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
        department_list = Department.objects.all()
        if management.power == '1':
            power = '1'
            management_list = Management.objects.all().order_by('job_no')
        else:
            management_list = Management.objects.filter(~Q(job_no='')).order_by('job_no')
        # 分页
        count = len(management_list)
        return render(request, 'management/manager_info.html', locals())

def update_management(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        management = Management.objects.get(id=id)
        job_no = management.job_no
        #只查询有职位的部门
        position_list = Position.objects.values('department').distinct()
        ids = []
        for i in position_list:
            ids.append(i['department'])
        department_list = Department.objects.filter(id__in = ids)

        return render(request,'management/management_update.html',locals())
    elif request.method == 'POST':
        myfile = None
        try:
            myfile = request.FILES['myfile']
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            file_path = os.path.join(os.path.join(BASE_DIR, 'static/files'), myfile.name)
            if myfile:
                with open(file_path, 'wb') as f:
                    data = myfile.file.read()
                    f.write(data)
        except Exception as e:
            print(e)
        #入职数据插入员工表
        id = request.POST.get('id')
        management = Management.objects.get(id = id)
        #获取前台数据
        #工号
        job_no = request.POST.get('job_no')
        management.job_no = job_no
        #部门
        dep_id = request.POST.get('dep_name')
        dep = Department.objects.get(id = dep_id)
        management.department_id = dep_id
        management.dep_name = dep.name
        #职位
        position_id = request.POST.get('position_name')
        position = Position.objects.get(id = position_id)
        management.position_id = position_id
        management.position_name = position.name
        #姓名
        name = request.POST.get('name')
        management.name = name
        #图片路径
        if myfile:
            management.img = '/static/files/'+myfile.name
        #性别
        sex = request.POST.get('sex')
        management.sex = sex
        #入职时间
        create_time = datetime.datetime.now()
        management.create_time = create_time
        management.save()
        # 获取用户名
        username = request.session.get("username")
        user = User.objects.filter(username=username)[0]
        management = Management.objects.filter(user=user)[0]
        # 管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
        department_list = Department.objects.all()
        if management.power == '1':
            power = '1'
            management_list = Management.objects.all().order_by('job_no')
        else:
            management_list = Management.objects.filter(~Q(job_no='')).order_by('job_no')
        # 分页
        count = len(management_list)
        return render(request, 'management/manager_info.html', locals())


def get_position(request):
    # 获取传入数据
    received_json_data = json.loads(request.body)
    dep_id = received_json_data['dep_id']
    department_list = Department.objects.all()
    data = {}
    if dep_id:
        department = Department.objects.get(id=dep_id)

        position_list = Position.objects.filter(department=department)
    else:
        position_list = Position.objects.all()


    data['position'] = json.loads(serializers.serialize("json", position_list))
    data['department'] = json.loads(serializers.serialize("json", department_list))
    return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
def delete_management(request):
    # 获取传入数据
    received_json_data = json.loads(request.body)
    del_management = Management.objects.filter(id=received_json_data['id'])
    del_user = User.objects.filter(username=del_management[0].username)

    # 作为一个事务
    try:
        with transaction.atomic():
            try:
                del_user.delete()
                del_management.delete()
            except Exception as e:
                print('---错误---')
                print(e)
                msg = ''
                raise DatabaseError

    except DatabaseError:
        return render(request, 'user/register.html', locals())

    # 获取用户名
    username = request.session.get("username")
    user = User.objects.filter(username=username)[0]
    management = Management.objects.filter(user=user)[0]
    # 管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
    department_list = Department.objects.all()
    if management.power == '1':
        power = '1'
        management_list = Management.objects.all().order_by('job_no')
    else:
        management_list = Management.objects.filter(~Q(job_no='')).order_by('job_no')
    #分页
    count = len(management_list)
    return render(request, 'management/manager_info.html', locals())

def search_management(request):
    #获取用户名
    username = request.session.get("username")
    user = User.objects.filter(username = username)[0]
    management = Management.objects.filter(user = user)[0]

    # 管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
    if management.power == '1':
        power = '1'
        management_list = Management.objects.all()
    else:
        management_list = Management.objects.filter(~Q(job_no=''))
    print(len(management_list),'=======11==')
    # 设置字典传入filter
    search_dict = {}
    name = request.POST.get('name')
    job_no = request.POST.get('job_no')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    dep_id = request.POST.get('dep_name')
    position_id = request.POST.get('position_name')

    if name:
        search_dict['name__startswith'] = name
    if job_no:
        search_dict['job_no__startswith'] = job_no
    if start_time:
        res = re.findall(r'(\d*)年(\d*)月(\d*)日',start_time)[0]
        start_date =  datetime.date(int(res[0]), int(res[1]), int(res[2]))
        search_dict['create_time__gte'] = start_date
    if end_time:
        res = re.findall(r'(\d*)年(\d*)月(\d*)日',end_time)[0]
        end_data =  datetime.date(int(res[0]), int(res[1]), int(res[2]) + 1)
        search_dict['create_time__lt'] = end_data
    if dep_id:
        search_dict['department_id'] = dep_id
        dep_name = Department.objects.get(id=dep_id).name
    if position_id:
        print('======3===')
        search_dict['position_id'] = position_id
        position_name = Position.objects.get(id=position_id).name
    management_list = management_list.filter(**search_dict).order_by('job_no')
    print(len(management_list), '=======22==',search_dict.keys())
    #查询部门
    department_ids = Position.objects.values('department').distinct()
    ids = []
    for i in department_ids:
        ids.append(i['department'])
    department_list = Department.objects.filter(id__in=ids)

    # 分页
    count = len(management_list)
    return render(request,'management/manager_info.html',locals())
