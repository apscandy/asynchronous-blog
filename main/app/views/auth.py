from fastapi import APIRouter

authentication = APIRouter(prefix="/auth")

@authentication.get("/", tags=["auth"])
async def auth_test():
    return {"Test":"Testing"}