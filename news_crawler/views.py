from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def listNews(request):
	context = News.objects.all()
	response = {
        "context" : context
    }
	return render(request, 'listNews.html', response)

def addNews(request):
    if(request.method == "POST"):
        crawlerName = request.POST.get("crawlerName")
        site = request.POST.get("site")
        startDate = request.POST.get("startDate")
        catchUp = request.POST.get("catchUp")
        News.objects.create(crawler_name=crawlerName, site=site, start_date=startDate, catch_up=catchUp)
        return redirect('listNews')
    else :
        return render(request, 'addNews.html')

def editNews(request, id):
    news = get_object_or_404(News, id=id)

    response = {
        "news" : news
    }

    if(request.method == "POST"):
        crawlerName = request.POST.get("crawlerName")
        site = request.POST.get("site")
        startDate = request.POST.get("startDate")
        catchUp = request.POST.get("catchUp")
        News.objects.filter(id=id).update(crawler_name=crawlerName, site=site, start_date=startDate, catch_up=catchUp)
        return redirect('listNews')
    else :
        return render(request, 'editNews.html', response)

def deleteNews(request, id):
	news = get_object_or_404(News, id=id)
	news.delete()
	return redirect('listNews')
