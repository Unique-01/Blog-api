from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer,UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


