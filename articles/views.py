from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/index.html', {'articles': articles})
    # return HttpResponse("Hello, world. You're at the articles index.")

def article_detail(request, slug):
    return HttpResponse(slug)