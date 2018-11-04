from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from forum.models import Post
from forum.forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(
        request,
        'forum/forum.html',
        {
            'title': 'home',
        }
    )


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/forum.html'


@login_required()
def create_post(request):
    form = PostForm()
    if form.is_valid():
        form.save()
    else:
        return render(request, 'forum/forum.html', {'form': form})
