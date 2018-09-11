# poor-twitter
A simple app to create tweet-like messages. Made with Vue.js, Django and django-rest-framework.


# Installation

Install git and clone this repo. Install Python3 and Pip, then:
```
  $ pip install -r requirements.txt
```

For better results, try using a [pyenv](https://github.com/pyenv/pyenv) and [virtualenv](https://github.com/pyenv/pyenv-virtualenv).

Once installed all dependencies, run DB migrations:
```
  $ python manage.py migrate
```

# Using guide

Then run local server by:
```
  $ python manage.py runserver 0.0.0.0:8000
```

Last, use a browser and try the app: `http://0.0.0.0:8000/app`
