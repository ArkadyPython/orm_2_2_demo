from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.order_by('-published_at')}
    return render(request, template, context)
