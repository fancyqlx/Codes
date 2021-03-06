from django.conf.urls import url

from . import views
app_name = "blog"
urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    url(r'^blog/view/(?P<slug>[^\.]+)/$', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+)/$', views.view_category, name='view_blog_category'),
]