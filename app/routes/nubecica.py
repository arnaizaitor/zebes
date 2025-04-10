from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def root_nubecica():
    return JSONResponse(content={"message": "Nubecica mock root OK"})
