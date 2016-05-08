from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stops/$', views.stops_list),
    url(r'^stops/(?P<pk>.*)/$', views.stops_detail),
]

