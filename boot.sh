#!/bin/bash
# this script is used to boot a Docker container
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:
export FLASK_ENV=development
export FLASK_DEBUG=0


exec python bjoern_dolgoe.wsgi.py
#exec python app.py
