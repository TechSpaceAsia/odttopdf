odt_to_pdf
==========

A Celery shared task to transform an odt file (or its UTF8-decoded representation) to PDF

Installation
------------

`pip install odt_to_pdf`

Usage
-----

### Creating task

See `examples/consumer/main.py`

Worker
======

The package works with a Celery worker which can be run directly `celery -A worker worker -Q odt_to_pdf -l INFO`

However this requires `libreoffice` to be installed.

It is therefore advisable to run the worker in Docker using this image: techspaceasia/odt_to_pdf:1.0.0

The worker needs to be run in an environment which has access to
- the Celery broker
- the Celery result backend
- The `libreoffice` executable

Development
===========

0. Create a network which will be accessible to both the worker and the task setter e.g.: `docker network create odt_to_pdf_network`
1. Run `redis` in that network .g. `docker run --rm --name redis --network odt_to_pdf_network redis:7.0.4` 
2. Build the docker image: `docker build -f docker/Dockerfile -t odt_to_pdf_worker:latest .`
3. Run the worker in the same network, optionally mounting the code into it `docker run -v $PWD:/code --network odt_to_pdf_network odt_to_pdf_worker:latest watchmedo auto-restart --directory=./odttopdf --pattern="*.py" --recursive -- celery -A worker worker -Q odttopdf -l INFO`
4. Create tasks from any other container which has access to the same network (you may reuse the worker image e.g. `docker run --rm --network odt_to_pdf_network -v $PWD:/code odt_to_pdf_worker:latest python examples/consumer/main.py`)


```
pip install watchdog
export CELERY_CONFIG_MODULE=celeryconfig_local
watchmedo auto-restart --directory=./odttopdf --pattern="*.py" --recursive -- celery -A worker worker -Q odttopdf -l INFO
```