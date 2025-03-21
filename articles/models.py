from django.db import models

# Create your models here.
class Article(models.Model):
    # 모델 자체는 단수
    # 게시물이라는 정의를 하는 공간이기 때문에 
     # 의미적으로 단수
    title = models.CharField(max_length=100)
    content =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 데이터가 저장되는 최초의 순간의 시간 정보를 저장
    updated_at = models.DateTimeField(auto_now=True)
    # 데이터가 저장되는 순간의 사간 정보를 저장
