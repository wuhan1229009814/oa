from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^list$',timebook_view),
    url(r'^check$',check_view),
    url(r'^month$',month_view),
    url(r'^update$',update_view),
    url(r'^insert$',insert_view),
]