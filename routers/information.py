from fastapi import APIRouter, HTTPException, Depends, UploadFile
from sqlalchemy.orm import Session
from functions.information import create_information, update_information, delete_information
from models.information import Information
from models.users import Users
from routers.login import get_current_active_user
from db import database

router = APIRouter(
    prefix="/information",
    tags=["Information operation"]
)


@router.get("/get_all")
def get(db: Session = Depends(database)):
    try:
        return db.query(Information).all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get_information_by_lessone_id")
def get_information_by_lesson_id(lesson_id: int, db: Session = Depends(database)):
    try:
        return db.query(Information).filter(Information.lesson_id == lesson_id).all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create")
def create_informations(description: str, example: UploadFile, lesson_id: int, db: Session = Depends(database),
                       current_user: Users = Depends(get_current_active_user)):
    try:
        return create_information(description, example, lesson_id, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.put("/update")
def update(ident: int, description: str, example: UploadFile, lesson_id: int, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return update_information(ident, description, example, lesson_id, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.delete("/delete")
def delete(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_active_user)):
    try:
        return delete_information(ident, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))
