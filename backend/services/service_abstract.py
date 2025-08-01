from abc import ABC, abstractmethod
from typing import List, Optional, Dict


class ChatServiceBase(ABC):
    # === CHAT ===
    @abstractmethod
    def chat(self, prompt: str, file_ids: Optional[List[str]] = None) -> str:
        """
        Sends a prompt (and optionally a list of file IDs) to the underlying AI model.
        Returns the response as a string.
        """
        pass

    # === DOCUMENTS ===
    @abstractmethod
    def list_documents(self) -> List[Dict]:
        """
        Returns a list of all available documents that have been uploaded.
        Each document should contain metadata such as file_id, filename, and created_at.
        """
        pass

    @abstractmethod
    def upload_document(self, file_path: str, filename: Optional[str] = None) -> Dict:
        """
        Uploads a document to the AI provider's file storage.
        Returns metadata including file_id and filename.
        """
        pass

    @abstractmethod
    def delete_document(self, file_id: str) -> bool:
        """
        Deletes a document from the AI provider's storage by its file ID.
        Returns True if the deletion was successful.
        """
        pass

    @abstractmethod
    def get_document_metadata(self, file_id: str) -> Dict:
        """
        Retrieves metadata for a specific document by its file ID.
        Useful for displaying detailed document information without exposing the file content.
        """
        pass
