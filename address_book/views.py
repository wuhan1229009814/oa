from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from index.views import logging_check
from management.models import Management


@logging_check
def address_book_list(request):
    """通讯录模块"""
    if request.method == "GET":
        users = Management.objects.all()
        all_user = []
        for user in users:
            if user.create_time:
                all_user.append(user)
        count = len(all_user)
        return render(request, "address_book/YuanGonglist.html", locals())
    elif request.method == "POST":
        department = request.POST.get("department")
        query = request.POST.get("query")
        if not query and not department:
            return HttpResponseRedirect("/address_book/list")
        elif query and not department:
            all_user = Management.objects.filter(name=query)
            if not all_user:
                all_user = Management.objects.filter(phone=query)
        elif not query and department:
            all_user = Management.objects.filter(dep_name=department)
        else:
            all_user = Management.objects.filter(name=query, dep_name=department)
            if not all_user:
                all_user = Management.objects.filter(phone=query, dep_name=department)
        count = len(all_user)
        return render(request, "address_book/YuanGonglist.html", locals())

