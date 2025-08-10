
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse




def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    new_app = FastAPI(title="FastAPI Application", version="1.0.0")
    # Allow CORS for local frontend
    new_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return new_app

app = create_app()


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application!"}

# New hello endpoint
from fastapi import Query

@app.get("/hello")
async def hello(name: str = Query("world", description="Name to greet")):
    return JSONResponse({"message": f"Hello, {name}!"})


