from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from shop.apps import ShopConfig
from shop.views import ProductListView, ProductDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='edit_post'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
]