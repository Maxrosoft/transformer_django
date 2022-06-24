from django.urls import path
from . import views 


app_name = 'main'
urlpatterns = [
    path('', views.maindata, name='maindata'),
    path('about_us/', views.aboutusdata, name='aboutusdata'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
] 