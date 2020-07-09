from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list_and_create),
    path('<int:item_pk>/', views.item_detail_update_delete),
    path('comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_update_and_delete),
]