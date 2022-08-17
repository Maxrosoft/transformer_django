from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'main'
urlpatterns = [
    path('', views.maindata, name='maindata'),
    path('about_us/', views.aboutusdata, name='aboutusdata'),
    path('posts/', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
] 