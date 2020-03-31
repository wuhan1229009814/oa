from django.conf.urls import url

from management import views

urlpatterns = [
    url(r'^list$',views.management_list),
    url(r'^add_management',views.add_management),
    url(r'^update_management',views.update_management),
    url(r'^get_position', views.get_position),
    url(r'^delete', views.delete_management),
    url(r'^search', views.search_management),
]