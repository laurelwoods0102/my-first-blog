from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

def post_list(request):
    posts = Post.objects.all().order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

class blogImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
