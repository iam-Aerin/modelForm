# articles 폴더 안에 내가 추가해준 파일입니다.

from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'