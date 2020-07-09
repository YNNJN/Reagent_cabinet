from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Item, Comment

class ItemSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Item
        fields = ('id', 'name', 'stock', 'location', 'created_at', 'updated_at', 'user', 'image',)
        read_only_fields = ('id', 'user', 'created_at', 'updated_at',)

class ItemListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Item
        fields = ('id', 'title', 'user',)

class ItemDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Item
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'updated_at',)
        read_only_fields = ('id', 'user', 'updated_at',)


