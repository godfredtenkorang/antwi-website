
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from users.forms import CommentForm
from users.models import Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'posts': Post.objects.all(),
        'blogs': Blog.objects.all()
    }
    return render(request, 'folio/index.html', context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request, 'folio/about.html', context)

def service(request):
    context = {
        'title': 'service',
        'services': Service.objects.all()
    }
    return render(request, 'folio/service.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'folio/contact.html')
    return render(request, 'folio/contact.html')

def posts(request):
    context = {
        'title':'Blog',
        'blog_posts': BlogPost.objects.all()
    }
    return render(request, 'folio/post.html', context)

class BlogPostListView(ListView):
    model = BlogPost
    template_name = "folio/post.html"
    context_object_name = "blog_posts"
    ordering = ["-date_posted"]
    paginate_by = 10


class BlogPostDetailView(DetailView):
    model = BlogPost

    form = CommentForm

    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context =  super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comment_count': post_comments_count,
        })
        return context
    

def book_now(request):
    return render(request, 'folio/booking.html')