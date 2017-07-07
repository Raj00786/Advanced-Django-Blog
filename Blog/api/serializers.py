from rest_framework.serializers import ModelSerializer
from blogs.models import Post

class PostSerializers(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'pk',
			'title',
			'slug',
			'content',
			'image',
		]
