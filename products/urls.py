from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import  ProductDetailView, ProductListView, VariationListView
from . import views
from django_messages.views import *

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^enquiry/$', 'django_messages.views.enquiry', name='enquiry'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    url(r'^enquiry/(?P<recipient>[\w.@+-]+)/$', enquiry, name='messages_compose_to'),
    url(r'^host/$', views.list, name='list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.post_detail_list, name='post_detail_list'),
    url(r'^list/detail/$', views.list_detail, name='list_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit_list, name='post_edit_list'), 
    #url(r'^service/$', views.service, name='service'),
    #url(r'^service/(?P<pk>[0-9]+)/$', views.post_detail_service, name='post_detail_service'),
    
    #url(r'^service/(?P<pk>[0-9]+)/edit/$', views.post_edit_service, name='post_edit_service'),

]
