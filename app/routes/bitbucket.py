from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def root_bitbucket():
    return JSONResponse(content={"message": "Bitbucket mock root OK"})
