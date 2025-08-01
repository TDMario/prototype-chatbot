# backend/core/exceptions.py

from typing import Optional


class ServiceError(Exception):
    """
    A unified application-level error class that can be raised by any service.
    Returns a standardized error message and optional error code.
    """
    def __init__(self, message: str, code: int = 500, details: Optional[dict] = None):
        self.message = message
        self.code = code
        self.details = details or {}
        super().__init__(message)

    def to_dict(self) -> dict:
        return {
            "error": self.message,
            "code": self.code,
            "details": self.details
        }