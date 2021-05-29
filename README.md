# react_django

```
python3 -V
Python 3.8.6
python3 -m venv venv_django
source venv_django/bin/activate
(venv_django) which python
/Users/takahashifuyuki/work/Git/react_django/venv_django/bin/python
(venv_django)
```

```
(venv_django) python -m pip list
Package    Version
---------- -------
pip        20.2.1
setuptools 49.2.1
WARNING: You are using pip version 20.2.1; however, version 21.1.2 is available.
You should consider upgrading via the '/Users/takahashifuyuki/work/Git/react_django/venv_django/bin/python -m pip install --upgrade pip' command.

(venv_django) python -m pip install --upgrade pip
Collecting pip
  Using cached pip-21.1.2-py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.1
    Uninstalling pip-20.2.1:
      Successfully uninstalled pip-20.2.1
Successfully installed pip-21.1.2
(venv_django)
```

```
(venv_django) takahashifuyuki@MacMini-FT react_django % python -m pip install djangorestframework
Collecting djangorestframework
  Downloading djangorestframework-3.12.4-py3-none-any.whl (957 kB)
     |████████████████████████████████| 957 kB 4.7 MB/s
Collecting django>=2.2
  Downloading Django-3.2.3-py3-none-any.whl (7.9 MB)
     |████████████████████████████████| 7.9 MB 9.7 MB/s
Collecting pytz
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 56.4 MB/s
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.3.2
  Downloading asgiref-3.3.4-py3-none-any.whl (22 kB)
Installing collected packages: sqlparse, pytz, asgiref, django, djangorestframework
Successfully installed asgiref-3.3.4 django-3.2.3 djangorestframework-3.12.4 pytz-2021.1 sqlparse-0.4.1
(venv_django) takahashifuyuki@MacMini-FT react_django % python -m pip list
Package             Version
------------------- -------
asgiref             3.3.4
Django              3.2.3
djangorestframework 3.12.4
pip                 21.1.2
pytz                2021.1
setuptools          49.2.1
sqlparse            0.4.1
(venv_django) takahashifuyuki@MacMini-FT react_django %
```

```
(venv_django) takahashifuyuki@MacMini-FT react_django % django-admin startproject music_controller
(venv_django) takahashifuyuki@MacMini-FT react_django % cd music_controller
(venv_django) takahashifuyuki@MacMini-FT music_controller % django-admin startapp api
```

music_controller/music_controller/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework'
]
```

music_controller/api/urls.py

```
from django.urls import path
from .views import main

urlpatterns = [
    path('', main)
]


```

# アプリを初めて実行する場合、view・データベース更新された時にコマンド実行する

python ./manage.py makemigrations
