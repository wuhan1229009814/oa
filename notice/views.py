"""通知公告模块"""
from django.core.paginator import Paginator
from django.shortcuts import render
from index.views import logging_check
from notice.models import Notice_list
from management.models import Management
from django.http import HttpResponseRedirect


# Create your views here.
@logging_check
def notice_list(request):
    if request.method == "GET":
        # 全部公告列表显示
        uid = request.session.get("uid")
        management = Management.objects.get(user_id=uid)
        all_notice = Notice_list.objects.all().order_by("-created_time")
        count = len(all_notice)
        return render(request, "notice/notice_list.html", locals())
    elif request.method == "POST":
        uid = request.session.get("uid")
        management = Management.objects.get(user_id=uid)
        query = request.POST.get("query")
        if not query:
            return HttpResponseRedirect("/notice/list")
        all_notice = Notice_list.objects.filter(title__contains=query)
        count = len(all_notice)
        return render(request, "notice/notice_list.html", locals())


@logging_check
def notice_add_view(request):
    # 添加公告
    if request.method == "GET":
        return render(request, "notice/notice_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        try:
            Notice_list.objects.create(title=title, content=content)
        except Exception as e:
            print("---添加失败---")
            print(e)
        return HttpResponseRedirect("/notice/list")


@logging_check
def notice_view(request):
    # 当前公告内容显示
    id = request.GET.get("id")
    try:
        notice = Notice_list.objects.get(id=id)
    except Exception as e:
        print(e)
    return render(request, "notice/notice.html", locals())


@logging_check
def notice_update_view(request):
    # 修改公告
    if request.method == "GET":
        id = request.GET.get("id")
        try:
            notice = Notice_list.objects.get(id=id)
        except Exception as e:
            print(e)
        return render(request, "notice/notice_update.html", locals())
    elif request.method == "POST":
        id = request.GET.get("id")
        try:
            notice = Notice_list.objects.get(id=id)
        except Exception as e:
            print(e)
            return HttpResponseRedirect("/notice/list")
        title = request.POST.get("title")
        content = request.POST.get("content")
        try:
            notice.title = title
            notice.content = content
        except Exception as e:
            print("---修改失败---")
            print(e)
        notice.save()
        return HttpResponseRedirect("/notice/list")


@logging_check
def notice_delete_view(request):
    # 删除公告
    id = request.GET.get("id")
    try:
        notice = Notice_list.objects.filter(id=id)
        notice.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect("/notice/list")
