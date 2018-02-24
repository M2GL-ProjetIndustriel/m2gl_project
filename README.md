# m2gl_project
[![Build Status](https://travis-ci.org/M2GL-ProjetIndustriel/m2gl_project.svg?branch=master)](https://travis-ci.org/M2GL-ProjetIndustriel/m2gl_project)
[![Coverage Status](https://coveralls.io/repos/github/M2GL-ProjetIndustriel/m2gl_project/badge.svg?branch=master)](https://coveralls.io/github/M2GL-ProjetIndustriel/m2gl_project?branch=master)
[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/M2GL-ProjetIndustriel/m2gl_project)

## Up and running

- Install virtualenvwrapper.
```bash
$ pip install virtualenvwrapper
```
- Create a new environment for the project/ or start the environment if already created.
```bash
$ mkvirtualenv -p /usr/bin/python3 proj-ind-backend
$ workon proj-ind-backend
```
- Install the dependencies for the project with pip within this environment.
```bash
pip install -r requirements.txt
```
- Start the server.
```bash
$ python app_server/manage.py runserver
```
- **RTFM**
