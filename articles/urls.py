from django.urls import path
from . import views
# from .views import index
# 같은 표현법

# index 라는 함수를 가져다 쓰겠다다

app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name='index'),

    # Create
    path('create/', views.create, name='create'),
]