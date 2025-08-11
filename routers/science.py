from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import database
from functions.science import create_science, update_science, delete_science
from models.science import Science
from models.users import Users
from routers.login import get_current_active_user
from schemas.science import SchemaScience

router = APIRouter(
    prefix="/science",
    tags=["Science operation"]
)


@router.get("/get_all")
def get(db: Session = Depends(database)):
    try:
        return db.query(Science).all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create")
def create_sciences(form: SchemaScience, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_active_user)):
    try:
        return create_science(form, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.put("/update")
def update(ident: int, form: SchemaScience, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return update_science(ident,form, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.delete("/delete")
def delete(ident: int, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return delete_science(ident, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))