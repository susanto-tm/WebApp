from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
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

# # CreatePost class not valid in urls
class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/forum.html'

    def create_post(request):
        if form.is_valid():
            form.save()
        else:
            return render(request, 'forum/forum.html', {'form': form})

class PostDetailView(DetailView):
    model = Post
    # slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

    # def post(self,)


def post_detail(request, slug):
    template = 'forum/forum-post.html'

    post = get_object_or_404(Post, slug=slug)
    context = {'post':post,}
    return render(request, template, context)


# @login_required()
# def create_post(request):
#     title = form.cleaned_data['title']
#     form = PostForm(request.POST)
#     model = Post
#     if form.is_valid():
#         form.save()
#         return render(request, 'forum/forum-post.html', {'post':post,})
#     else:
#         return render(request, 'forum/forum.html', {'form': form})

