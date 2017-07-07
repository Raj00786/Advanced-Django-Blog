from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework import permissions
from blogs.models import Post
from .serializers import PostSerializers
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User


class BlogListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializers
	lookup_field= 'name'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BlogDetailAPIView(ListAPIView):
	serializer_class = PostSerializers
	lookup_field= 'slug'
	lookup_url_kwarg = 'byname'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_queryset(self):
		name = self.kwargs.get(self.lookup_url_kwarg)
		data = Post.objects.filter(slug=name)
		return data

class BlogUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializers
	lookup_field= 'title'
	lookup_url_kwarg = 'byname'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BlogDestroyAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializers
	lookup_field= 'title'
	lookup_url_kwarg = 'byname'	
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

