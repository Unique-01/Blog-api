from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.api_root),
    path('posts/',views.PostList.as_view(),name="post-list"),
    path('posts/<int:pk>/',views.PostDetail.as_view(),name='post-detail'),
    path('users/',views.UserList.as_view(),name="user-list"),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('comments/',views.CommentList.as_view(),name='comment-list'),
    path('comments/<int:pk>/',views.CommentDetail.as_view(),name='comment-detail'),
    # path('get-csrf-token/',views.get_csrf_token,name='get-csrf-token'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)