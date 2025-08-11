from fastapi import APIRouter, HTTPException, Depends, UploadFile
from sqlalchemy.orm import Session
from functions.lesson import create_lesson, update_lesson, delete_lesson
from models.lesson import Lesson
from models.users import Users
from routers.login import get_current_active_user
from db import database

router = APIRouter(
    prefix="/lesson",
    tags=["Lesson operation"]
)


@router.get("/get_all")
def get(science_id: int = None, db: Session = Depends(database)):
    try:
        if science_id:
            return db.query(Lesson).filter(Lesson.science_id == science_id).all()
        return db.query(Lesson).all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create")
def create_lessons(name: str, icon: UploadFile, science_id: int, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_active_user)):
    try:
        return create_lesson(name, icon, science_id, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.put("/update")
def update(ident: int, name: str, icon: UploadFile, science_id: int, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return update_lesson(ident, name, icon, science_id, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.delete("/delete")
def delete(ident: int, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return delete_lesson(ident, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))
