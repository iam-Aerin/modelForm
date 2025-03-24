from django.urls import path
from . import views
# from .views import index
# 같은 표현법

# index 라는 함수를 가져다 쓰겠다다

app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name='index'),
    path('<int:id>/',views.detail,name='detail'),

    # Create
    path('create/', views.create, name='create'),

    # Comment Create
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    
    # Comment Delete
    path('<int:article_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete'),

]
