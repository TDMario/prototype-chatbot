# backend/api/routes_services.py

from fastapi import APIRouter
from backend.services.service_registry import SERVICE_REGISTRY

router = APIRouter()

@router.get("/")
def list_services():
    return list(SERVICE_REGISTRY.keys())
