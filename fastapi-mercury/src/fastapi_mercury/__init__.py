from fastapi import FastAPI
from .__about__ import __version__
from .routes import shipments

app = FastAPI()
app.include_router(shipments.router)

@app.get('/')

def status() -> dict:
    return {
        'status': 'ok',
        'version': __version__
    }