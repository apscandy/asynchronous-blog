from fastapi import APIRouter

blog = APIRouter(prefix="/blog")

@blog.get("/", tags=["blog"])
async def auth_test():
    return {"Test":"Testing"}