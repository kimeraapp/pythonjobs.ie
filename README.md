# pythonjobs.ie
Python jobs: find or post Python related jobs without registration.

[![Build Status](https://travis-ci.org/kimeraapp/pythonjobs.ie.svg?branch=master)](https://travis-ci.org/kimeraapp/pythonjobs.ie)

[![Coverage Status](https://coveralls.io/repos/kimeraapp/pythonjobs.ie/badge.svg?branch=master&service=github)](https://coveralls.io/github/kimeraapp/pythonjobs.ie?branch=master)

![pythonjobs_ie](https://cloud.githubusercontent.com/assets/6503912/10180230/5493706a-6703-11e5-8c31-39b93e2d3fd9.png)

##Development

###Environment

If you don't have Python you can follow the instructions from https://www.python.org/downloads/.

First, create an environment. 
```
$ virtualenv env
```
You can activate it.
```
$ source ./env/bin/activate
```
When not using you can deactivate it.
```
$ deactivate
```
###Django and PostgreSQL

Install Django.

```
$ pip install django
```
Install Python PostgreSQL dependencies.
```
$ apt-get install libpq-dev python-dev
$ apt-get install postgresql postgresql-contrib
```
Create pythonjobs database.
```
$ sudo su - postgres
$ createdb pythonjobs
```
Export database.
```
$ export DATABASE_URL=postgres://development:development@127.0.0.1:5432/pythonjobs
```

###Project

Fork the repository and clone into you local computer.

```
$ git clone git@github.com:MYUSERNAME/pythonjobs.ie.git
$ cd pythonjobs.ie
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver 0.0.0.0:8000
```

###Development guidelines
Always create a new branch for the new feature/issue.
```
$ git checkout -b feature-name-branch
```
Then make your changes and commit. Last of the commit could include the issue number in the message, like: fixes #1 or closes #1.
```
$ git commit -am 'descriptive message about the issue'
```
Push the branch to your Github account.
```
$ git push origin feature-name-branch
```
Now go to Github and make the pull request. Add a descriptive comment and you can include 'Resolve #1' to close the issue when the pull request is merged.
