from django.urls import path
from .views import BlogPostListView, BlogPostDetailView
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('post/', BlogPostListView.as_view(), name='post-page'),
    path('blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('service/', views.service, name='service-page'),
    path('contact/', views.contact, name='contact-page'),
    path('book/', views.book_now, name='book-page'),
]