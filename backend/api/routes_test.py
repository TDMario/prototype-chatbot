from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/test_ping")
async def test_ping():
    return JSONResponse(content={"message": "pong"})