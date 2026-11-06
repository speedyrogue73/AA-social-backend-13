from django.shortcuts import render
from django.views import View
from .models import Post


class HomeView(View):
    def get(self, request):
        posts = Post.objects.filter(is_published=True)
        return render(request, 'home/index.html', {'posts': posts})
