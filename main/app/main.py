from typing import Union
from fastapi import FastAPI
from views.auth import authentication
from views.blog import blog
import uvicorn

app = FastAPI()
app.include_router(authentication)
app.include_router(blog)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)