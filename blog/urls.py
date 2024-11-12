from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('add/',PostCreateView ,name='add-post'),
    path('edit/<int:id>/',PostUpdateView,name='edit-post'),
    path('delete/<int:id>/',PostDeleteView,name='delete-post'),
]