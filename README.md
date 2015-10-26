# pythonjobs.ie
Python jobs: find or post Python related jobs without registration.

[![Build Status](https://travis-ci.org/kimeraapp/pythonjobs.ie.svg?branch=master)](https://travis-ci.org/kimeraapp/pythonjobs.ie)

[![Coverage Status](https://coveralls.io/repos/kimeraapp/pythonjobs.ie/badge.svg?branch=master&service=github)](https://coveralls.io/github/kimeraapp/pythonjobs.ie?branch=master)

![pythonjobs_ie](https://cloud.githubusercontent.com/assets/6503912/10180230/5493706a-6703-11e5-8c31-39b93e2d3fd9.png)

##Development

###Environment

If you don't have Python you can follow the instructions from https://www.python.org/downloads/.

Make sure to install Python 3.x instead of the default 2.x

First, create an environment.
```
$ virtualenv env
```
If you have both python 2.x and 3.x versions, use the below command.
```
$ virtualenv --python=/usr/bin/python3 env
```
You can activate it.
```
$ source ./env/bin/activate
```
Verify the version of python from the 1st line by the below command.
```
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
When not using you can deactivate it.
```
$ deactivate
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
Then make your changes and commit. Last of the commit could include the issue number in the message, like: fixes #1 or closes #1. Add yourself to the CONTRIBUTORS file.
```
$ git commit -am 'descriptive message about the issue'
```
Please check always that he tests are running before pushing anything, you might consider to fix it before making the pull request. Add tests when possible for your own code and test that the app works accordingly.
```
$ ./manage.py test
```
Push the branch to your Github account.
```
$ git push origin feature-name-branch
```
To keep sync with the main repository you will have to add it as a second repository. This will only be available for pulling the latest changes.
```
$ git remote add upstream https://github.com/kimeraapp/pythonjobs.ie.git
$ git pull upstream master
```
Now go to Github and make the pull request. Add a descriptive comment and you can include 'Resolve #1' to close the issue when the pull request is merged.

If you the pull request has conflicts you have to pull from the upstream, fix them and just push to your remote branch again. There is no need to make another pull request.

###Code styling
PEP8 is used in this project. Please make sure you follow the documentation: https://www.python.org/dev/peps/pep-0008/.

4 spaces are used for Python identation and 2 for the HTML templates and CSS.

Setup your line limit to 80 chars.

Instead of comments use descriptive names and keep consistency with the current style. You can explain better either in the commit message or the pull request description, but the code should be easy to review. When in doubt, please feel free to comment on the issue.
