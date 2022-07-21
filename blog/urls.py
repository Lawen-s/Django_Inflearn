from django.urls import path
from . import views


app_name = 'blog' # URL Reverse에서 namespace 역할을 하게 된다.


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
