from django.conf.urls import url, include
from django.contrib import admin

from index import views

urlpatterns = [
    url(r'^index', views.index_views),
    url(r'^my_info$', views.index_my_info),
    url(r'^my_ip$', views.index_my_ip),
    # url(r'^my_bj$', views.index_my_bj),
    url(r'^my_mim$', views.index_my_mim),
    url(r'^childapp=(\w*)&info=(\w*)$',views.child_view),
    url(r'^childapp=(\w*)&info=(\w*)&id=(\d*)',views.child_notice_view),
]