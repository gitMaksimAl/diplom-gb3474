import uvicorn
from app import app


if __name__ == '__main__':
    uvicorn.run("asgi:app", reload=True)
