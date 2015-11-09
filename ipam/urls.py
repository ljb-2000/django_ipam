from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^supernet/new/$', views.new_supernet,
        name='new_supernet'),
    url(r'^supernet/edit/(?P<supernet_id>[0-9]+)/$', views.edit_supernet,
        name='edit_supernet'),
    url(r'^supernet/delete/(?P<supernet_id>[0-9]+)/$', views.delete_supernet,
        name='delete_supernet'),
    url(r'^supernet/id/(?P<supernet_id>[0-9]+)/$', views.view_supernet,
        name='view_supernet'),
    url(r'^subnet/id/(?P<subnet_id>[0-9]+)/$', views.view_subnet,
        name='view_subnet')
]
