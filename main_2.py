import os

from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.otp_router import router as v1_otp_router

stage = os.environ.get('STAGE', None)
root_path = f"/{stage}" if stage else "/"
app = FastAPI(title="ServerlessOTPService", root_path=root_path)

app.include_router(v1_otp_router, prefix="/api/v1")

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

handler = Mangum(app)