from backend.services.default.service_default import DefaultService
from backend.services.s_prototype.service_prototype import PrototypeService

SERVICE_REGISTRY = {
    "default": DefaultService(),
    "openai": PrototypeService(),
}

DEFAULT_SERVICE_KEY = "default"
