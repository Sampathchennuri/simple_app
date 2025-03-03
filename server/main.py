from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI();

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend to access backend (modify for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def read_root() -> JSONResponse:
    return JSONResponse(content={"status": "Hello from Backend FastAPI server!!"});