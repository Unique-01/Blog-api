from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(view_name='post-detail',read_only=True,many=True)
    class Meta:
        model = User
        fields = ['url','id','username','posts']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    author = serializers.HyperlinkedIdentityField(view_name='user-detail')
    class Meta:
        model = Post
        fields= ['url','id','author','author_username','title','content']