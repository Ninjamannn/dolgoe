import bjoern
from app import app

bjoern.run(
    wsgi_app=app,
    host='0.0.0.0',
    port=5050,
    reuse_port=True
)
