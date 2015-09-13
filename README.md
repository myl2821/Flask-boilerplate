# Flask-boilerplate

A Flask boilerplate which
integrates ORM, UT and task manager Framework.

## Why not sinatra?

Sometimes we are required to use python instead of ruby.

## Prerequisites
* *nix (I have not tested it on windows)
* Python 2.7+
* Mysql-server(change sql server as you like)

## Install

```
	$ pip install -r requirements.txt
```

## Build database

```
	$ invoke db_init
```

## Run

```
	$ invoke serve
```
## Test

```
	$ py.test
```
