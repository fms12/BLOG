# DjangoBlog 
https://mayanks-blog.herokuapp.com/




A blog system based on `python3.8` and `Django3.0`.:


![Django](https://img.shields.io/pypi/djversions/djangorestframework?style=for-the-badge)   ![PYTHON](https://img.shields.io/pypi/pyversions/Django?style=for-the-badge)


![App Screenshot](https://i.ibb.co/Csk8YGY/Screenshot-56.png)

  
## Main Features:
- Articles, Pages, Categories, Tags(Add, Delete, Edit), edc. Articles and pages support `Markdown` and highlighting.
- Articles support full-text search.
- Complete comment feature, include posting reply comment and email notification. `Markdown` supporting.
- Sidebar feature: new articles, most readings, tags, etc.
- OAuth Login supported, including Google, GitHub, Facebook, Weibo, QQ.
- Simple SEO Features, notify Google and Baidu when there was a new article or other things.
- Simple picture bed feature integrated.
## RUN

Run the following commands in Terminal:
```bash
./manage.py makemigrations
./manage.py migrate
```

**Attention: ** Before you using `./manage.py`, make sure the `python` command in your system is towards to `python 3.6` or above version. Otherwise you may solve this by one of the two following methods:
- Modify the first line in `manage.py`, change `#!/usr/bin/env python` to `#!/usr/bin/env python3`
- Just run with: `python3 ./manage.py makemigrations`
### Create super user

Run command in terminal:
```bash
./manage.py createsuperuser
```

### Create testing data
Run command in terminal:
```bash
./manage.py create_testdata
```

### Collect static files
Run command in terminal:
```bash
./manage.py collectstatic --noinput
./manage.py compress --force
```

### Getting start to run server
Execute: `./manage.py runserver`

Open up a browser and visit: http://127.0.0.1:8000/ , the you will see the blog.
