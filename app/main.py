from fastapi import FastAPI

from app.users.router import router as router_users
from app.audiorecords.router import router as router_audiorecords

app = FastAPI()

app.include_router(router_users)
app.include_router(router_audiorecords)
