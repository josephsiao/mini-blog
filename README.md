# mini-blog

## Usage

安裝 [python 3.6](https://www.python.org/downloads/windows/) 與 `pipenv` 套件

```
$ pip3 install pipenv
```

設定 `pipenv` 虛擬環境

```
$ pipenv --python 3.6
```

進入虛擬環境

```
$ pipenv shell
```

透過 `Pipfile` 安裝所需套件

```
$ pipenv install
```

藉由 `manage.py` 來管理 Django 專案

處理資料庫

```
$ python manage.py makemigrations
$ python manage.py migrate
```

建立管理員

```
$ python manage.py createsuperuser
```

處理靜態檔案

先將 `settings.py` 裡的 `STATICFILES_DIRS` 註解(#)

```
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
```

接著

```
$ python manage.py collectstatic
```

再把 `settings.py` 裡的 `STATICFILES_DIRS` 的註解(#)拿掉

開啟伺服器

```
$ python manage.py runserver
```

Done

## Recommend References

- [Python](https://docs.python.org/3.6/)
- [Django 3 documentation](https://docs.djangoproject.com/en/3.0/)
- [Bootstrap 4 documentation](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
- [Select2](https://select2.org/)
- [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor)
- [Django Bleach](https://github.com/marksweb/django-bleach)
- [Toastr](https://github.com/CodeSeven/toastr)
