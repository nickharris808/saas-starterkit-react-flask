from fastapi import APIRouter, Depends, HTTPException
from src.middlewares.authMiddleware import get_current_user
from src.models.user import User
from src.controllers import userController, billingController

router = APIRouter()

def admin_only(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

@router.get("/users")
async def get_all_users(current_user: User = Depends(admin_only)):
    return await userController.get_all_users()

@router.get("/billing")
async def get_all_billing_info(current_user: User = Depends(admin_only)):
    return await billingController.get_all_billing_info()