# StudyHive

## Setup

* The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/JasbirCodeSpace/StudyHive.git
$ cd StudyHive
```
* Install virtualenvwrapper

```sh
pip install virtualenvwrapper
```
* Create a virtual environment to install dependencies in and activate it:

```sh
$ mkvirtualenv studyhive
$ workon studyhive
```

* Then install the dependencies:

```sh
(studyhive)$ pip install -r requirements.txt
```
* Note the `(studyhive)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenvwrapper`.

* Once `pip` has finished downloading the dependencies:
```sh
(studyhive)$ python manage.py runserver
```

## Database Migrations

propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema

```sh
(studyhive)$ python manage.py makemigrations
(studyhive)$ python manage.py migrate
```
