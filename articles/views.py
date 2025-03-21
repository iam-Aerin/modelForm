from django.shortcuts import render, redirect
# redirect사용할거니까 import에 추가하기

from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # index 페이지의 목표는 전체 데이터를 읽는 것이므로
    # 전체 데이터를 가져와야한다.
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)
# 이후 articles 폴더 안에 templates라는 폴더를 생성한뒤 그 안에 index.html을 만들어준다. 


def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터 저장하는 기능
    # ==================================
    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 시용자가 입력한 데이터를 저장하는 기능
    # 하나의 종이에 두 기능을 함께 처리

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # 정보가 유효하다면  저장해라
        else:
            context = {
                'form' : form,
            }
        # 유효하지않다면, 알려주자
            return render(request, 'create.html', context)

    else:
        # 빈종이를 보여주는 기능을 여기에 짠다.
        # return render(request, 'create.html')
        #  이렇게 해왔지만, 이번에는 forms.py를 활용해서 코드를 짠다. 일일히 html을추가해주지 않아도 되게
        form = ArticleForm()
        context = {
            'form' : form,
        }

        return render(request, 'create.html', context)