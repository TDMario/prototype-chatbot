# backend/api/routes_chat.py

from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from backend.services.service_registry import SERVICE_REGISTRY, DEFAULT_SERVICE_KEY
from backend.core.exceptions import ServiceError

router = APIRouter()

class ChatInput(BaseModel):
    prompt: str
    file_ids: Optional[List[str]] = None

@router.post("/")
async def chat(request: Request, body: ChatInput):
    try:
        service_key = request.query_params.get("service", DEFAULT_SERVICE_KEY)
        service = SERVICE_REGISTRY.get(service_key, SERVICE_REGISTRY[DEFAULT_SERVICE_KEY])
        response = service.chat(prompt=body.prompt, file_ids=body.file_ids)
        return {"response": response}
    except ServiceError as e:
        raise HTTPException(status_code=e.code, detail=e.to_dict())
