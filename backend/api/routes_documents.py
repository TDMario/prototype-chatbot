# backend/api/routes_documents.py

from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from backend.services.service_registry import SERVICE_REGISTRY, DEFAULT_SERVICE_KEY
from backend.core.exceptions import ServiceError
import os

router = APIRouter()

@router.get("/")
async def list_documents(request: Request):
    try:
        service_key = request.query_params.get("service", DEFAULT_SERVICE_KEY)
        service = SERVICE_REGISTRY.get(service_key, SERVICE_REGISTRY[DEFAULT_SERVICE_KEY])
        return service.list_documents()
    except ServiceError as e:
        raise HTTPException(status_code=e.code, detail=e.to_dict())

@router.post("/")
async def upload_document(request: Request, file: UploadFile = File(...)):
    try:
        service_key = request.query_params.get("service", DEFAULT_SERVICE_KEY)
        service = SERVICE_REGISTRY.get(service_key, SERVICE_REGISTRY[DEFAULT_SERVICE_KEY])

        os.makedirs("temp_uploads", exist_ok=True)

        # Temporäre Speicherung auf Disk (Pfad kann angepasst werden)
        file_location = f"temp_uploads/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        return service.upload_document(file_path=file_location, filename=file.filename)
    except ServiceError as e:
        raise HTTPException(status_code=e.code, detail=e.to_dict())

@router.delete("/{file_id}")
async def delete_document(request: Request, file_id: str):
    try:
        service_key = request.query_params.get("service", DEFAULT_SERVICE_KEY)
        service = SERVICE_REGISTRY.get(service_key, SERVICE_REGISTRY[DEFAULT_SERVICE_KEY])
        success = service.delete_document(file_id=file_id)
        return {"deleted": success}
    except ServiceError as e:
        raise HTTPException(status_code=e.code, detail=e.to_dict())
