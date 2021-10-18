# `Robots Competition` service

`Robots Competition` service is a RESTful web service that allows engineers (aka commanders) register competitions for robots that are
grouped into robot categories.

## FEATURES
* Filtering and Searching  
* Ordering and Pagination
* Authentication and Permissions
* Throttling
* Versioning Management
* Tests

## RESTFUL ROUTES

```text
|Endpoints                  |HTTP Method   |CRUDMethod   |Result   |
|---------------------------|--------------|-------------|---------|
|/robot-categories/         |    GET       |     READ    | get all robot categories
|/robot-categories/         |    POST      |     CREATE  | add a robot category
|/robot-category/:id/       |    GET       |     READ    | get a single robot category
|/robot-category/:id/       |    PUT       |     UPDATE  | update an existing robot category
|/robot-category/:id/       |    PATCH     |     UPDATE  | update one or more fields of an existing robot category
|/robot-category/:id/       |    DELETE    |     DELETE  | delete a robot category
|/robot/                    |    GET       |     READ    | get all robots
|/robot/                    |    POST      |     CREATE  | add a robot
|/robot/:id/                |    GET       |     READ    | get a single robot
|/robot/:id/                |    PUT       |     UPDATE  | update an existing robot
|/robot/:id/                |    PATCH     |     UPDATE  | update one or more fields of an existing robot
|/robot/:id/                |    DELETE    |     DELETE  | delete a robot
|/commander/                |    GET       |     READ    | get all commanders
|/commander/                |    POST      |     CREATE  | add a commander
|/commander/:id             |    GET       |     READ    | get a single commander
|/commander/:id             |    PUT       |     UPDATE  | update an existing commander
|/commander/:id             |    PATCH     |     UPDATE  | update one or more fields of an existing commander
|/commander/:id             |    DELETE    |     DELETE  | delete a commander
|/competitions/             |    GET       |     READ    | get all competitions
|/competitions/             |    POST      |     CREATE  | add a competition
|/competitions/:id/         |    GET       |     READ    | get a single competition
|/competitions/:id/         |    PUT       |     UPDATE  | update an existing competition
|/competitions/:id/         |    PATCH     |     UPDATE  | update one or more fields of an existing competition
|/competitions/:id/         |    DELETE    |     DELETE  | delete a competition
```

## General Usage

* Clone the repository
* Create a virtual environment in the folder. (If you are on linux, use the command below):
```bash
 python3.9 -m venv venv
```
* Activate the virtual environment (If you are on linux, use the command below):
```bash
 source venv/bin/activate
```
* Install the requirements:
```bash
 pip install -r requirements.txt
```
* Make migrations:
```bash
 python manage.py makemigrations api
 python manage.py migrate
```
* Run the command below to run the tests
```
 pytest
```
* Run the DJANGO's server and access the endpoints
```
 python manage.py runserver
```