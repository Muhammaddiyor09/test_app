from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import database
from functions.test import create_test, update_test, delete_test
from models.test import Test
from models.users import Users
from routers.login import get_current_active_user
from schemas.test import SchemaTest

router = APIRouter(
    prefix="/test",
    tags=["Test operation"]
)


@router.get("/get_all")
def get(db: Session = Depends(database)):
    try:
        return db.query(Test).all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create")
def create_test(form: SchemaTest, db: Session = Depends(database),
                current_user: Users = Depends(get_current_active_user)):
    try:
        return create_test(form, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.put("/update")
def update(ident: int, form: SchemaTest, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return update_test(ident, form, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.delete("/delete")
def delete(ident: int, db: Session = Depends(database),
           current_user: Users = Depends(get_current_active_user)):
    try:
        return delete_test(ident, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))