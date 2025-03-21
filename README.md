    # ModelForm
    모델: 데이터베이스의 구조를 정의할 때
    Form: 사용자에게 데이터를 입력받기 위한 (input, textbox -> submit)

    데이터와 데이터를 입력 받기 위한 form => modelform

    ---
# Django

## 0. setting

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