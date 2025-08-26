from django.shortcuts import render, get_object_or_404
from .models import Topic, Article

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'core/topic_list.html', {'topics': topics})

def topic_detail(request, topic_slug):
    topic = get_object_or_404(Topic, slug=topic_slug)
    articles = topic.articles.all()
    return render(request, 'core/topic_detail.html', {'topic': topic, 'articles': articles})

def article_detail(request, topic_slug, article_slug):
    article = get_object_or_404(Article, slug=article_slug, topic__slug=topic_slug)
    return render(request, 'core/article_detail.html', {'article': article})
