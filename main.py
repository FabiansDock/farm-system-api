from fastapi import FastAPI
from farm_app import router as farm_app

app = FastAPI(
    title="Farm System API",
    summary="",
    description="",
    version="0.0.1",
    contact={
        "name": "Fabian Dcruz"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(farm_app.router)

@app.get('/', tags=["root"])
def root():
    return {"message": "Welcome to Farm System API"}