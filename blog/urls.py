from django.urls import path
from .views import Bloghome, Blogdetails, AddPost,UpdatePost,DeletePost

app_name = 'blog'

urlpatterns = [
    path('', Bloghome.as_view(), name='bloghome'),
    path('blogdetails/<int:pk>', Blogdetails.as_view(), name='blogdetails'),
    # path('blogdetails/<slug:slug>', Blogdetails.as_view(), name='blogdetails'),
    # path('add_post/', AddPost.as_view(), name='add_post'),
    # path('edit_post/<slug:slug>', UpdatePost.as_view(), name='edit_post'),
    # path('delete_post/<slug:slug>/remove', DeletePost.as_view(), name='delete_post'),
    # # path('like/<int:pk>', LikeView, name='like_post'),
]
