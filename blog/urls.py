
from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
   
    path('', HomePageView3.as_view() , name="index"),

    path('download/<int:article_id>', download , name="download"),

    path('test', TestView.as_view(), name="test"),

    path('search', search, name="search"),
    path('article/<int:pk>', ArticleDeteilView.as_view() , name="detail"),
    path('category/<int:category_id>', category_articles, name="category_articles" ),
    path('signer/<int:signer_id>', signer_sounds ),
]
