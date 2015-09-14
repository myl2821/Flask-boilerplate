# Flask-boilerplate

A Flask boilerplate which
integrates ORM, UT and task manager.

## Why not Sinatra?

Sometimes we are required to use python instead of ruby.

## Prerequisites
* *nix (I have not tested it on windows)
* Python 2.7+
* Mysql-server(change sql server as you like)

## Install

```
	$ sudo pip install virtualenv
	$ virtualenv venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt
```

## Build database

```
	$ source venv/bin/activate
	$ invoke db_init
```

## Run

```
	$ source venv/bin/activate
	$ invoke serve
```
## Test

```
	$ source venv/bin/activate
	$ py.test
```

## Deployment

	Deploy using gunicorn and gevent.

```
	$ invoke gunicorn_start
	$ invoke gunicorn_stop
	$ invoke gunicorn_restart
```
