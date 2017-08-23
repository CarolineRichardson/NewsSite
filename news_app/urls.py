from django.conf.urls import patterns, include, url
from django.contrib import admin

from news_app.views import register,welcome,brickout, create, articles, article, loggedIn, logout, main

from django.contrib.auth.views import login, logout
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'news_n_stuff.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^brickout/$',brickout),
    url(r'^team/$',brickout),
    url(r'^main/$',main),
    url(r'^accounts/login/$',login),
    url(r'^loggedIn/$',loggedIn),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',welcome),
    url(r'^all/$', 'news_app.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'news_app.views.article'),
    url(r'^create/$', 'news_app.views.create'),
    url(r'^articles/create/$', 'news_app.views.create'),
    url(r'^articles/all/$', 'news_app.views.articles'),
    url(r'^like/(?P<article_id>\d+)/$', 'news_app.views.like_article'),
    url(r'^show/(?P<messages_id>\d+)/$', 'news_app.views.show_messages'),
    url(r'^delete/(?P<messages_id>\d+)/$', 'news_app.views.delete_messages'),



)






