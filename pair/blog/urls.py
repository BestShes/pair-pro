from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'detail/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'add/$', views.post_add, name='post_add'),
]