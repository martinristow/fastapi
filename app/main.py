from fastapi import FastAPI
from app import models
from app.database import engine
from .routes import post, user, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine) -> now we don't want this because we used alembic to generate our tables

app = FastAPI()

# origins = ["https://www.google.com"]  # If we want to give permission to only some parties to have access
origins = ["*"]  # If we want to give permission to all parties to have access

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "welcome to my api!"}
