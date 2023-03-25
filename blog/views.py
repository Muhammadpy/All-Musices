



from django.shortcuts import render,redirect,get_object_or_404
import datetime
from .models import Category,Article,Singer
from fallowers.models import Fallower
from django.contrib.auth.models import User
from django.db.models import Q

from django.template.loader import get_template

from django.http import HttpResponse,HttpResponseRedirect,FileResponse, JsonResponse
from django.urls import reverse
from django.conf import settings

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View

# Create your views here.

today = datetime.date(2022,3,15)
today.year
today.month

class TestView(View):
    def get(self, request):
        company_name = "Andijon Broyler MCHJ 777"
        services = ["Tovuq go'shti","Do'mboq jo'ja","Yem maxsulotlari","Grill"]
        a = Article.objects.get(id=8)
        c = {"company":company_name,"services":services,"article":a}

        return render(request, "test.html", c)




class HomePageView3(View):

    def get(self, request):
        articles = Article.objects.all()
        # article = Article.objects.first()
        categories = Category.objects.all()
        signers = Singer.objects.all()
        print(articles)
  
        context = {
                    "articles":articles,
                    "categories":categories,
                    "signers":signers,
                     "language":"UZ",
                    #  "article":article
                    }
        return render(request, "index.html", context)

    def post(self, request):
        categories = Category.objects.all()
        signers = Singer.objects.all()
        query = request.POST['q']
        q = Q(name__contains=query) | Q(signer__name__contains=query) | Q(signer__surname__contains=query) | Q(category__name__contains=query)

        a = Article.objects.filter(q)
        context = {
                    "articles":a,
                    "categories":categories,
                    "signers":signers,
                   
                    }
        return render(request, "index.html", context)




class HomePageView2(ListView):
    template_name = "index.html"
    context_object_name = 'articles'
    queryset = Article.objects.all()
    
    # def get_queryset(self):
    #     return Article.objects.all()


class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        articles = Article.objects.all()
        categories = Category.objects.all()
        signers = Singer.objects.all()

        context['articles'] = articles
        context['categories'] = categories
        context['signers'] = signers
        return context



# @require_http_methods(["GET"])
# def function(request):
#     print( request.method == "POST" )
#     print( request.GET )
#     print( request.POST)

#     # a = get_object_or_404(Article, id=1542)
#     # Article.objects.get(id=4811)
#     # return redirect("blog:category_articles", category_id=11)
#     # data = {"status":"cancelled", "message_id": 1589} 
#     # return JsonResponse(data)   
#     # file = open(f"{settings.BASE_DIR}/static/js/bootstrap.min.js", 'rb')
#     # return FileResponse(file, as_attachment=True)

#     # return HttpResponseRedirect( 
#     #     reverse("blog:category_articles" , kwargs={"category_id":11 }) 
#     #      )

#     print()
#     # print(  reverse("blog:category_articles" , kwargs={"category_id":1 }) )
#     print()

#     articles = Article.objects.filter(view__lt=60)
#     articles = Article.objects.filter(view__lte=60)
#     articles = Article.objects.filter(view__gt=60)
#     articles = Article.objects.filter(view__gte=60)


#     articles = Article.objects.filter(id__range=(5,8))
#     articles = Article.objects.filter(view__range=(20,80))


#     articles = Article.objects.filter(reg_date__year=2022,
#                                             reg_date__month__range=(3,5) )
    
#     articles = Article.objects.filter(file__isnull=False)
#     articles = Article.objects.filter(id__in=(6,7,8))




#     articles = Article.objects.filter(id__in=(6,7,8))
#     articles = Article.objects.filter(category__name__icontains="lirika" )
#     articles = Article.objects.filter(category__name__startswith="li" )


#     # article = Article.objects.get(id=99)
#     article = Article.objects.first()
#     article = Article.objects.last()
#     article = Article.objects.latest('reg_date')
#     article = Article.objects.earliest('reg_date')

#     articles = Article.objects.filter(category__name__startswith="li" ).exists()

#     articles = Article.objects.filter(category__name__startswith="li" ).count()
#     articles = Article.objects.all().count()
#     articles = Article.objects.count()


#     articles = Article.objects.latest('reg_date')
#     articles = Article.objects.earliest('reg_date')
#     articles = Article.objects.values('name',"id")
#     articles = Article.objects.dates('reg_date','year')
#     articles = Article.objects.in_bulk([5,8,9,12,4], field_name='id')

#     articles = Article.objects.all()

#     print()
#     print()
#     print(articles)
#     print()
#     print()
                                    
#     # a = Article.objects.get(name='Bandaman')
#     # a.reg_date = datetime.date(2021,3,15)
#     # a.save()



#     categories = Category.objects.all()
#     signers = Singer.objects.all()
#     context = {
#                   "articles":articles,
#                  "categories":categories,
#                  "signers":signers
#                 }
#     return render(request, "index.html", context)
    

def article_detail(request,article_id):
    a = Article.objects.get(id=article_id)
    context = {'article':a}
    return render(request, "single-post.html",context)

class ArticleDeteilView(DetailView):
    model = Article
    context_object_name = 'a'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

def category_articles(request,category_id):

    print( request.GET , ' GET atribute from request')
    print( request.POST , ' POST atribute from request')
    print( request.method , ' method atribute from request')

    category = Category.objects.get(id=category_id)
    a = Article.objects.filter(category=category)
    categories = Category.objects.all()
    context = {"articles":a, "categories":categories}

    template = get_template('index.html')
    obj = HttpResponse(template.render(context=context, request=request))


    return obj 
    return render(request, "index.html", context)


def signer_sounds(request,signer_id):
    signers = Singer.objects.all()
    signer = Singer.objects.get(id=signer_id)
    articles = Article.objects.filter(signer=signer)
    categories = Category.objects.all()
    context = {
        "articles": articles,
            "categories":categories,
             "signers":signers
            }
    return render(request, "index.html", context)


def search(request):
    # print( request.GET , ' GET atribute from request')
    # print( request.POST , ' POST atribute from request')
    # print( request.method , ' method atribute from request')
    # print( request.headers , 'Meta atribute from request')
    # print( request.body , 'Meta atribute from request')
    # print( request.get_host() , '')
    # print( request.get_port() , '')
    # print( request.get_full_match() , '')
    # print( request.get_full_match() , '')
    print( request.is_secure() , '')
    print( request.is_ajax() , '')

    query = request.GET.get('q')
    # query = request.POST['q']
    print(query)
    # a = Article.objects.exlude(name="Sarson")


    # a = Article.objects.filter(name__icontains=query)

    # a = Article.objects.filter(name__exact=query)
    # a = Article.objects.filter(name__iexact=query)

    # a = Article.objects.exclude(name__startswith=query)

    
    # a = Article.objects.filter(name__istartswith=query)
    # a = Article.objects.filter(name__endswith=query)

    # a = Article.objects.filter(name__icontains=query,signer__name__contains=query)
    
    
    categories = Category.objects.all()
    signers = Singer.objects.all()

    q = Q(name__contains=query) | Q(signer__name__contains=query) | Q(signer__surname__contains=query) | Q(category__name__contains=query)

    a = Article.objects.filter(q)
    context = {
                  "articles":a,
                 "categories":categories,
                 "signers":signers
                }
    return render(request, "index.html", context)
         

def download(request,article_id):
    article = Article.objects.get(id=article_id)
    article_file_url = article.file.url
    print(article_file_url)  
    print(settings.BASE_DIR)
    abs_path = f"{settings.BASE_DIR}/{article_file_url}"
    file = open(abs_path,"rb")
    return FileResponse(file, as_attachment=True)


