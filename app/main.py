from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app import models
from app.database import engine
from .routes import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# request Get method url: "/"


while True:

    try:
        conn = psycopg2.connect(host='', database='', user='',
                                password='', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 5}]


def find_post(id):
    for p in my_posts:
        print(p)
        if p["id"] == id:
            print(p['id'])
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "welcome to my api!"}


# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#
#     posts = db.query(models.Post).all()
#     return {"data": posts}