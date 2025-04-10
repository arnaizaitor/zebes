from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def root_vault():
    return JSONResponse(content={"message": "Vault mock root OK"})
