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

## Requirements

```text
djangorestframework==3.12.4
Django==3.2.8
pytest-django==4.4.0
pytest==6.2.4
```