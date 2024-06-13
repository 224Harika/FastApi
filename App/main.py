from fastapi import FastAPI
from app.api.endpoints import configuration
from app.database import engine, Base

# Initialize the FastAPI app
app = FastAPI()

# Create all database tables
Base.metadata.create_all(bind=engine)

# Include the configuration router
app.include_router(configuration.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Configuration Management System"}
