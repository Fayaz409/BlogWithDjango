from django.urls import path
from . import views
from .views import PostView,DetailPost,CreatePost,UpdatePost,DeletePost,AddCategory,CategoryView,LikeView

urlpatterns = [
    path('',PostView.as_view(),name='home'),
    path('detail_post/<int:pk>',DetailPost.as_view(),name='detail_post'),
    path('create_post',CreatePost.as_view(),name='create_post'),
    path('article/edit/<int:pk>',UpdatePost.as_view(),name='update_post'),
    path('delete_post/<int:pk>/remove',DeletePost.as_view(),name='delete_post'),
    path('add_category/',AddCategory.as_view(),name='add_category'),
    path(route='category/<str:cats>/',view=CategoryView,name='category'),
    path('like/<int:pk>',views.LikeView,name='like_post'),

]