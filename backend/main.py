from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import routes_test
from backend.api.routes_chat import router as chat_router
from backend.api.routes_documents import router as documents_router
from backend.api.routes_services import router as services_router

app = FastAPI(title="LLM Chat Backend")

# CORS aktivieren (z. B. für Frontend-Fetch)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Demo-Zwecke offen lassen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === ROUTEN ===
app.include_router(routes_test.router, prefix="/test", tags=["test"])  # Optional für Ping etc.
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(documents_router, prefix="/documents", tags=["documents"])
app.include_router(services_router, prefix="/services", tags=["services"])

# Optional: Basisroute
@app.get("/")
def root():
    return {"message": "Backend is running. Available routes: /chat, /documents, /services, /test"}