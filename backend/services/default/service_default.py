from backend.services.service_abstract import ChatServiceBase
from typing import List, Optional, Dict

class DefaultService(ChatServiceBase):
    def chat(self, prompt: str, file_ids: Optional[List[str]] = None) -> str:
        return (
            "This is a default fallback service.\n"
            "To implement the actual chat functionality:\n"
            "1. Create a subclass of ChatServiceBase.\n"
            "2. Use OpenAI or another LLM provider.\n"
            "3. Implement the 'chat()' method to call the real API.\n"
            "4. Optionally, support file_ids for document context.\n"
            "5. Register the new service in backend/services/service_registry.py"
        )

    def list_documents(self) -> List[Dict]:
        return [{"file_id": "mock-id", "filename": "example.pdf", "created_at": "n/a"}]

    def upload_document(self, file_path: str, filename: Optional[str] = None) -> Dict:
        return {"status": "not implemented", "file_path": file_path}

    def delete_document(self, file_id: str) -> bool:
        return False

    def get_document_metadata(self, file_id: str) -> Dict:
        return {"status": "not implemented", "file_id": file_id}