from django.conf.urls import url

from department import views

urlpatterns = [
    url(r'^list$',views.department_list),
    url(r'^add_department',views.add_department),
    url(r'^add_position',views.add_position),
    url(r'^delete',views.delete_position),
    url(r'^del_department',views.delete_department),
    url(r'^update',views.department_update),
]