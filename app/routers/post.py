from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(prefix="/posts", tags=['Posts'])


@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.email)
    posts = db.query(models.Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(added_post: schemas.PostCreateUpdate, db: Session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.email) 
    new_post = models.Post(owner_id=current_user.id, **added_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.email)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    
    return post


@router.delete("/{id}", status_code=204)
def delete_post(id: int, db: Session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.email)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id:{id} was not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
        detail=f"Request is not allowed")
    
    post_query.delete(synchronize_session=False)
    
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostCreateUpdate, db: Session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):

    print(current_user.email)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exit")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
        detail=f"Request is not allowed")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    
    db.commit()
    return post_query.first()
    