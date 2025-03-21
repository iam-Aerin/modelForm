# ModelForm
    > 모델: 데이터베이스의 구조를 정의할 때
    >
    > Form: 사용자에게 데이터를 입력받기 위한 (input, textbox -> submit)

- 데이터와 데이터를 입력 받기 위한 form => modelform

    ---
# Django

0. setting

- `.gitignore`
- 가상환경 설정
    - `python -m venv venv`
    - `source venv/Scripts/activate`
- `README.md`

## 1. Django 프로젝트

1. django 설치
```shell
pip install django
```

2. 프로젝트 생성
```shell
django-admin startproject <pjt-name> <path>
```

3. 서버실행 (종료 : `ctrl + c`)
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app-name>
```

5. 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```

![](./MTV.png)
    ---

5-1. 모델 정의 (`models.py` 에서)

e.g. 

```python
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
```


6. 번역 작업 (`migration`) -> 파이썬 세상의 문법을 sql/  db에 적용이 가능하도록
```shell
python manage.py makemigrations
```

=> 만일 `model.py`의 내용에 변화가 있다면, 다시 `makemigrations`를 해야함. 

7. 데이터베이스 세상에 실제로 이주 (`migrate`)
```shell
python manage.py migrate
```

8. admin  등록
`admin.py'`에서 
`admin.site.register(Article)`

9. createsuperuser: admin 계정 만들기
```shell
python manage.py createsuperuser
```

10. server 실행
```shell
python manage.py runserver
```

+) 추가설정
`setting.py`에 추가적인 폴더 [`templates `] 도 찾아줘

외부에 `templates` 이라는 폴더를 생성하고고

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates' ],
```
=> `BASE_DIR / 'templates'` 를 추가함.