from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate



class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields= ['url','id','author','title','content','created_at','updated_at']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True,read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['url','id','username','posts','password']


