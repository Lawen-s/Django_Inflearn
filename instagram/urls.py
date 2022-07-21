from django.urls import path, re_path, register_converter
from . import views


class YearConberter:
    regex = r"20\d{2}"
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)

register_converter(YearConberter, 'year')

app_name = 'instagram' # URL Reverse에서 namespace 역할을 하게 된다.

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year), # url을 새로 만들어놓은 경우
    path('archives/<year:year>/', views.archives_year),
]