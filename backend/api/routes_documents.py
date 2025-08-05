# backend/api/routes_documents.py

from fastapi import APIRouter, Request, UploadFile, File, HTTPException
import os
from backend.services.service_registry import SERVICE_REGISTRY, DEFAULT_SERVICE_KEY
from backend.core.exceptions import ServiceError

router = APIRouter()

@router.get("/")
async def list_documents(request: Request):
    try:
        service_key = request.query_params.get("service", DEFAULT_SERVICE_KEY)
        service = SERVICE_REGISTRY.get(service_key, SERVICE_REGISTRY[DEFAULT_SERVICE_KEY])
        print(service.list_documents())
        return service.list_documents()
    except ServiceError as e:
        raise HTTPException(status_code=e.code, detail=e.to_dict())

@router.post("/")
async def upload_document(request: Request, file: UploadFile = File(...)):
    try:
        service_key = request.query_params.get("service", DEFAULT_SERVICE_KEY)
        service = SERVICE_REGISTRY.get(service_key, SERVICE_REGISTRY[DEFAULT_SERVICE_KEY])
        print("[UPLOAD] Using service:", service_key, type(service).__name__)

        # Stelle sicher, dass der Upload-Ordner existiert
        os.makedirs("temp_uploads", exist_ok=True)

        # Datei temporär speichern
        file_location = f"temp_uploads/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        result = service.upload_document(file_path=file_location, filename=file.filename)

        # Optional: lokale Datei direkt löschen
        os.remove(file_location)

        return result
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
