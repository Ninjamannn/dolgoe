import bjoern
from app import app


"""
alternative for gunicorn uwsgi server
very fast, very light
but it is not exactly :)
don`t forget install on your Ubuntu server: apt-get install libev-dev
"""
bjoern.run(
    wsgi_app=app,
    host='0.0.0.0',
    port=5000,
    reuse_port=True
)
