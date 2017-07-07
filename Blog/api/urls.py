from django.conf.urls import url
from django.contrib import admin
from .views import BlogListAPIView,BlogDetailAPIView,BlogUpdateAPIView,BlogDestroyAPIView

urlpatterns = [
    url(r'^$',BlogListAPIView.as_view(),name='blog_list'),

# for blogs
    url(r'^(?P<byname>[\w-]+)/$',BlogDetailAPIView.as_view(),name='detail'),
    url(r'^(?P<byname>[\w-]+)/update/$',BlogUpdateAPIView.as_view(),name='update'),
    url(r'^(?P<byname>[\w-]+)/delete/$',BlogDestroyAPIView.as_view(),name='delete'),

#for users
]