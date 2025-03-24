# articles 폴더 안에 내가 추가해준 파일입니다.

from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
        
class CommentForm(ModelForm):
    class Meta():
        model = Comment
        exclude = ('article',)
        
        # 왜 'article'을 exclude 했냐면...
        # 사용자 입력 방지: 폼에서 article 필드를 제외함으로써 
        # 사용자가 댓글을 어떤 게시글에 달지 직접 선택하지 않도록 합니다. 
        # 이는 보안상의 이유로 중요합니다.
        # =>  어떤 게시글에 댓글을 달지 다시 선택할 필요가 없습니다.