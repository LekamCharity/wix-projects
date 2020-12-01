from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='pages-home'),
    path('project/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('project/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('project/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('project/new/', PostCreateView.as_view(), name='post-create'),
]