# app/api/main.py
from fastapi import APIRouter
#from .auth.infrastructure.auth_controller import router as auth_router

api_router = APIRouter()

#api_router.include_router(auth_router, prefix="/auth", tags=["auth"])