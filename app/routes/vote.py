from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, schemas, oauth2
from app.database import get_db

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(votes: schemas.Vote, db: Session = Depends(get_db),
         current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(votes.post_id == models.Post.id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {votes.post_id} does not exist")

    vote_query = db.query(models.Vote).filter(votes.post_id == models.Vote.post_id,
                                              current_user.id == models.Vote.user_id)

    found_vote = vote_query.first()
    if votes.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted on post {votes.post_id}!")

        new_vote = models.Vote(post_id = votes.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Vote does not exist')

        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Successfully deleted vote"}