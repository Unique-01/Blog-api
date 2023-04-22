from rest_framework import serializers
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    authorId = serializers.PrimaryKeyRelatedField(source="author", read_only=True)

    class Meta:
        model = Post
        fields = [
            "url",
            "id",
            "author",
            "authorId",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    postId = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    authorId = serializers.PrimaryKeyRelatedField(source="author", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "url",
            "id",
            "postId",
            "author",
            "authorId",
            "content",
            "created_at",
            "updated_at",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["profile_picture"]


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "profile",
            "username",
            "first_name",
            "last_name",
            "posts",
        ]

    def update(self, instance, validated_data):
        profile_serializer = self.fields["profile"]
        try:
            profile_instance = instance.profile
        except Profile.DoesNotExist:
            profile_instance = Profile(user=self.request.user)
        profile_data = validated_data.pop("profile", {})

        profile_serializer.update(profile_instance, profile_data)

        instance = super().update(instance, validated_data)

        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile = ProfileSerializer
    posts = PostSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
            "posts",
            "first_name",
            "last_name",
            "password",
        ]
