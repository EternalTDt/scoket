from rest_framework import serializers
from .models import Post, Tag, Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('__all__')


class TagSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Tag
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('__all__')
