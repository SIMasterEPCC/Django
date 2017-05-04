from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^temperaturas/$', views.temperatura_list),
]