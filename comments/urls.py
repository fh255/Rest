from django.urls import path
from comments import views

urlpatterns = [
    path('posts/<int:post_pk>/comments/', views.CommentList.as_view(), name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]
