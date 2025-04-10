from fastapi import FastAPI
from app.routes import artifactory

app = FastAPI(title="ZEBES")

app.include_router(artifactory.router, prefix="/artifactory", tags=["Artifactory"])
