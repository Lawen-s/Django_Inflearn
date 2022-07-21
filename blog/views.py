from django.shortcuts import render
from .models import Post1

def post_list(request):
    qs = Post1.objects.all()
    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
    })