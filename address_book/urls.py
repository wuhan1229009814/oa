from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list$', views.address_book_list),
]
