"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('index.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^management/',include('management.urls')),
    url(r'^address_book/',include('address_book.urls')),
    url(r'^report/',include('report.urls')),
    url(r'^notice/',include('notice.urls')),
    url(r'^department/',include('department.urls')),
    url(r'^timebook/',include('timebook.urls'))
]