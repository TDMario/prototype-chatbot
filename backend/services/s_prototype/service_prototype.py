# backend/services/s_prototype/service_prototype.py

import os
from typing import List, Optional, Dict
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from backend.core.exceptions import ServiceError
from backend.services.service_abstract import ChatServiceBase

load_dotenv()  # Lade .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")

client = OpenAI(api_key=OPENAI_API_KEY)


class PrototypeService(ChatServiceBase):

    def chat(self, prompt: str, file_ids: Optional[List[str]] = None) -> str:
        try:
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=prompt,
                file_ids=file_ids or [],
            )

            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=ASSISTANT_ID,
            )

            # Warten bis abgeschlossen
            while True:
                run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
                if run.status == "completed":
                    break
                elif run.status in ["failed", "cancelled"]:
                    raise ServiceError("OpenAI run failed", code=500)
            
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            return messages.data[0].content[0].text.value.strip()

        except OpenAIError as e:
            raise ServiceError(f"OpenAI API error: {str(e)}", code=500)

    def list_documents(self) -> List[Dict]:
        try:
            files = client.files.list()
            return [{"id": f.id, "filename": f.filename, "created_at": f.created_at} for f in files.data]
        except OpenAIError as e:
            raise ServiceError(f"Failed to list documents: {str(e)}", code=500)

    def upload_document(self, file_path: str, filename: Optional[str] = None) -> Dict:
        try:
            with open(file_path, "rb") as f:
                uploaded_file = client.files.create(file=f, purpose="assistants")
            return {"id": uploaded_file.id, "filename": uploaded_file.filename}
        except OpenAIError as e:
            raise ServiceError(f"Failed to upload document: {str(e)}", code=500)

    def delete_document(self, file_id: str) -> bool:
        try:
            result = client.files.delete(file_id)
            return result.deleted
        except OpenAIError as e:
            raise ServiceError(f"Failed to delete document: {str(e)}", code=500)

    def get_document_metadata(self, file_id: str) -> Dict:
        try:
            f = client.files.retrieve(file_id)
            return {"id": f.id, "filename": f.filename, "created_at": f.created_at}
        except OpenAIError as e:
            raise ServiceError(f"Failed to retrieve file metadata: {str(e)}", code=500)
