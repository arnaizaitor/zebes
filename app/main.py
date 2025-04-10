from fastapi import FastAPI
from app.routes import artifactory, bitbucket, nubecica, vault

app = FastAPI(
    title="ZEBES",
    description="Zone for Emulated Behavior of External Services",
    version="0.1.0",
    contact={
        "name": "SAMUS Team",
        "email": "samus@airbus.com"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)


app.include_router(artifactory.router, prefix="/artifactory", tags=["Artifactory"])
app.include_router(bitbucket.router, prefix="/bitbucket", tags=["Bitbucket"])
app.include_router(nubecica.router, prefix="/nubecica", tags=["Nubecica"])
app.include_router(vault.router, prefix="/vault", tags=["Vault"])