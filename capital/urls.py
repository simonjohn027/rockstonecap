from django.conf.urls import url

from . import views


urlpatterns= [
    url(r'^$',views.index,name ='index'),

    url(r'dash/(?P<user_id>[0-9]+)/$',views.dashboardView, name = 'dashboard'),

    url(r'about/$',views.about, name ='about')

    ]