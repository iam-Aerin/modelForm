from django.shortcuts import render, redirect
# redirect사용할거니까 import에 추가하기

from .models import Article, Comment
from .forms import ArticleForm, CommentForm



def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터 저장하는 기능
    # ==================================
    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 시용자가 입력한 데이터를 저장하는 기능
    # 하나의 종이에 두 기능을 함께 처리
	
	# 모든 경우의 수
	# - GET : form 을 만들어서  html 문서를 사용자에게 리턴
	# - POST: invalid data(데이터 검증 실패)
	# - POST: valid data ()


# 5. POST 요청 (invalid data)

# 10. Post 요청 (재) (valid data)
	if request.method == 'POST':

		# 6. 사용자가 입력한 데이터 (request.POST) 가 invalid함 => 그걸 담은 form을 생성
		
		# 11. 사용자가 입력한 데이터 (request.POST)가 valid함 => 그걸 담은 form을 생성
		form = ArticleForm(request.POST)


		# 7. form 을 검증 (실패)
		# 12. form 을 검증 (성공 => if 문 안으로 들어간다.)

		if form.is_valid():
			# 13. form 저장

			form.save()
			return redirect('articles:index')
			# 14. index로 redirect해라.

		# 정보가 유효하다면  저장해라
	   
	# 1. GET 요청
	else:
		# 빈종이를 보여주는 기능을 여기에 짠다.
		# return render(request, 'create.html')
		#  이렇게 해왔지만, 이번에는 forms.py를 활용해서 코드를 짠다. 일일히 html을추가해주지 않아도 되게
		# 2. 비어있는 form을 만든다.
		form = ArticleForm()
	
	# 3. context dict에 비어있는 form 을 담는다.

	# 8. invalid한 데이터가 담긴 form (context dixct에 검증에 실패한 form을 담는다.)
	context = {
		'form': form,
	}


	# 4. create.html.dm을 랜더링

	# 9. create.html을 랜더링
	return render(request, 'create.html', context)


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

def detail(request, id):
    article = Article.objects.get(id=id)
    comments = article.comment_set.all()
    
    form = CommentForm()
    
    context = {
		'article' : article,
        'form' : form,
        'comment': comments,
  
	}
    
    return render(request, 'detail.html', context)

# Comment Create 함수 만들기
def comment_create(request, article_id):
       if request.method == 'POST':
              form = CommentForm(request. POST)
              if form.is_valid():
                     comment = form.save(commit=False)
                     article = Article.objects.get(id=article_id)
                     comment.article = article
                     comment.save()
                     
                     return redirect('articles:detail', id=article_id)
       else:
              return redirect('articles:index')
       
       
# Comment Delete 함수 만들기
def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('articles:detail', id=article_id)
