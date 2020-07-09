from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Item, Comment
from .serializers import ItemSerializer, ItemListSerializer, ItemDetailSerializer, CommentSerializer

@api_view(['GET', 'POST'])
def item_list_and_create(request):
    def index(request):
        items = Item.objects.all()
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)

    def create(request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

    if request.method == 'POST':
        return create(request)
    else:
        return index(request)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def item_detail_update_delete(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    def detail(request, item_pk):
        serializer = ItemDetailSerializer(item)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def update(request, item_pk):
        if request.user == item.user:
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def delete(request, item_pk):
        if request.user == item.user:
            item.delete()
        return Response()

    if request.method == 'GET':
        return detail(request, item_pk)
    elif request.method == 'PUT':
        return update(request, item_pk)
    else:
        return delete(request, item_pk)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, item=item)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_and_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    def comment_update(request):
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response

    def comment_delete(request):
        if request.user == comment.user:
            comment.delete()
        return Response()

    if request.method == 'PUT':
        return comment_update(request)
    else:
        return comment_delete(request)

