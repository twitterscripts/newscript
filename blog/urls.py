from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^feed/$', views.post_list, name='post_list'),
    url(r'^reports/$', views.report_list, name='report_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^report/new/$', views.report_new, name='report_new'),
    url(r'^$', views.the_script, name='the_script'),
    ]