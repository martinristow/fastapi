from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()


# request Get method url: "/"

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "welcome to my api!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}



@app.post('/createposts')
def create_posts(post: Post):
    # print(new_post.rating)
    # print(new_post)
    print(post.dict())
    return {"data": post}
# title str, content str