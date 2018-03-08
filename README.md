# m2gl_project
[![Build Status](https://travis-ci.org/M2GL-ProjetIndustriel/m2gl_project.svg?branch=master)](https://travis-ci.org/M2GL-ProjetIndustriel/m2gl_project)
[![Coverage Status](https://coveralls.io/repos/github/M2GL-ProjetIndustriel/m2gl_project/badge.svg?branch=master)](https://coveralls.io/github/M2GL-ProjetIndustriel/m2gl_project?branch=master)
[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/M2GL-ProjetIndustriel/m2gl_project)

## Up and running (Nix)

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

## Windows  

### Installation
1. Create the env in a different directory.   
    `$ pipenv --three`
2. Install requirements.  
    `$ pipenv install -r requirements.txt`
3. Use the env  
    `$ pipenv shell`
4. Install postgresql [(here !)](https://www.openscg.com/bigsql/postgresql/installers.jsp/)    
5. Setup postgresql.  

    - USER: toto  
    - PASSWORD: azert  
    - Rights: superuser + createdb  
    - Create a table called 'experiments_db'  
    - The DB should be accessible on localhost:5432.  

### Setup DB
1. Create migration   
    `$ python app_server/manage.py makemigrations api`
2. Install migration  
    `$ python app_server/manage.py migrate`
    
## Populate database with dummy values

To initialize the database use the following command:

`$ python manage.py loaddata ./api/fixtures/db.json`

## Empty Database

`$ python manage.py flush`

## Save current state of the database

`$ python manage.py dumpdata ./api/fixtures/db.json`

