from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.api_root),
    path('posts/',views.PostList.as_view(),name="post-list"),
    path('posts/<int:pk>/',views.PostDetail.as_view(),name='post-detail'),
    path('users/',views.UserList.as_view(),name="user-list"),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)