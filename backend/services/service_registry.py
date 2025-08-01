from backend.services.default.service_default import DefaultService
from backend.services.openai.service_openai import OpenAIService

SERVICE_REGISTRY = {
    "default": DefaultService(),
    "openai": OpenAIService(),
}

DEFAULT_SERVICE_KEY = "default"
