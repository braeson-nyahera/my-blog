from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('add/',PostCreateView ,name='add-post'),
    path('edit/<int:id>/',PostUpdateView,name='edit-post'),
]