from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post, MainData, AboutUsData


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'main/posts/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'main/posts/post/detail.html',
                  {'post': post})


def maindata(request):
    md = MainData.published.all()[0]
    return render(request, 'main/mainpage/base.html', {'md': md})


def aboutusdata(request):
    aud = AboutUsData.published.all()[0]
    return render(request, 'main/aboutUs/base.html', {'aud': aud})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'main/posts/post/list.html'
