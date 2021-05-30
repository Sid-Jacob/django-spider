from django.urls import path, re_path

from . import views
# from . import views, testdb

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin, admindocs

from Likes import urls as Lik_urls
from Comment import urls as Com_urls
admin.autodiscover()

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login),
    path('news/', views.news),
    path('news_list/', views.news_list),
    path('search_list/', views.search_list),
    path('spider/', views.spider),
    url(r'', include(Com_urls)),
    url(r'^likes/', include(Lik_urls)),
]
