import json
import time

from django.shortcuts import render

# Create your views here.
from department.models import Department, Position
from management.models import Management


def department_list(request):
    """部门信息"""
    position_list = Position.objects.all().order_by('dep_name')
    #分页
    count = len(position_list)
    return render(request,'department/BuMenGL_list.html',locals())

def add_department(request):
    if request.method == 'GET':
        return render(request,'department/BuMenGL_bmtj.html',locals())
    elif request.method == 'POST':
        position_list = Position.objects.all().order_by('dep_name')
        # 分页
        count = len(position_list)
        dep_name = request.POST.get('dep_name')
        if dep_name:
            time.sleep(2)
            try:
                dep_old = Department.objects.filter(name=dep_name)
                if dep_old:
                    msg = "已经存在该部门"
                    return render(request, 'department/BuMenGL_bmtj.html', locals())

                dep = Department.objects.create(name= dep_name)

            except Exception as e:
                print('---添加失败---')
                print(e)
                msg = '添加失败'
                return render(request, 'department/BuMenGL_list.html', locals())
        msg = '添加成功'

        return render(request, 'department/BuMenGL_list.html', locals())

def add_position(request):
    if request.method == 'GET':
        department_list = Department.objects.all()
        return render(request,'department/BuMenGL_zwtj.html',locals())
    elif request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        description = request.POST.get('description')
        position_name = request.POST.get('position_name')

        if dep_name and description and position_name:
            try:
                department = Department.objects.filter(name = dep_name)[0]
                position_old = Position.objects.filter(name= position_name,dep_name = dep_name)
                if position_old:
                    msg = "已经存在该部门该职位"
                    department_list = Department.objects.all()
                    return render(request, 'department/BuMenGL_zwtj.html', locals())

                position = Position.objects.create(name= position_name,dep_name = dep_name,description = description,
                                                   department = department)

            except Exception as e:
                print('---添加失败---')
                print(e)
                msg = '添加失败'
                return render(request, 'department/BuMenGL_list.html', locals())
        msg = '添加成功'

        position_list = Position.objects.all().order_by('dep_name')
        # 分页
        count = len(position_list)
        return render(request, 'department/BuMenGL_list.html', locals())


def delete_position(request):

    time.sleep(0.5)
    #获取传入数据
    received_json_data=json.loads(request.body)
    del_position = Position.objects.filter(id=received_json_data['id'])
    del_position.delete()

    #展示页面
    position_list = Position.objects.all().order_by('dep_name')
    #分页
    count = len(position_list)
    return render(request,'department/BuMenGL_list.html',locals())

def delete_department(request):

    if request.method == 'GET':
        department_list = Department.objects.all()
        return render(request, 'department/BuMenGL_bmsc.html', locals())
    elif request.method == 'POST':
        dep_id = request.POST.get('dep_id')
        department_list = Department.objects.all()
        position_list = Position.objects.all().order_by('dep_name')
        # 分页
        count = len(position_list)
        if dep_id:
            try:
                dep = Department.objects.get(id=dep_id)
                if not dep:
                    msg = "不存在该部门"
                    return render(request, 'department/BuMenGL_bmsc.html', locals())
                management_list = Management.objects.filter(department_id = dep_id)
                if len(management_list) > 0:
                    msg = "该部门还有员工存在，先删除员工，再删除部门"
                    return render(request, 'department/BuMenGL_bmsc.html', locals())
                dep.delete()

            except Exception as e:
                print('---添加失败---')
                print(e)
                msg = '添加失败'
                return render(request, 'department/BuMenGL_list.html', locals())
        msg = '添加成功'

        return render(request, 'department/BuMenGL_list.html', locals())


def department_update(request):

    if request.method == 'GET':
        # 获取传入数据
        id = request.GET.get('id')
        name = request.GET.get('name')
        dep_name = request.GET.get('dep_name')
        description = request.GET.get('description')
        print(id,name,dep_name,description)

        return render(request, 'department/BuMenGL_bmxg.html', locals())
    elif request.method == 'POST':
        #修改数据
        id = request.POST.get('id')
        dep_name = request.POST.get('dep_name')
        description = request.POST.get('description')
        position_name = request.POST.get('name')
        if id and dep_name and description and position_name:
            position_one = Position.objects.filter(id=id)[0]
            position_one.dep_name = dep_name
            position_one.description = description
            position_one.name = position_name
            position_one.save()
        #展示页面
        position_list = Position.objects.all().order_by('dep_name')
        #分页
        count = len(position_list)
        return render(request,'department/BuMenGL_list.html',locals())
