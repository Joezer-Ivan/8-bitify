from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.upload_file),
    url(r'^bye/$', views.bye),
]
