from django.conf.urls import url

from report import views

urlpatterns = [
    url(r"^list$",views.list),
    url(r"^add$",views.add),
    url(r"^update/(\d+)$",views.update),
    url(r"^delete/(\d+)$",views.delete),
    url(r"^content$",views.content),
]
