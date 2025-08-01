from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import routes_test

app = FastAPI()

# CORS (Frontend ←→ Backend lokal)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Demo-Zwecke offen lassen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router laden
app.include_router(routes_test.router)