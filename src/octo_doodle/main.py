from fastapi import FastAPI



def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    new_app = FastAPI(title="FastAPI Application", version="1.0.0")


    return new_app

app = create_app()

@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application!"}


