from models.science import Science


def create_science(form, db, carent_user):
    if carent_user.role != "admin":
        return {"message": "siz admin emassiz"}
    science = Science(name=form.name)
    db.add(science)
    db.commit()
    return {"message": "science yaratildi"}


def update_science(ident, form, db, carent_user):
    if carent_user.role != "admin":
        return {"message": "siz admin emassiz"}
    db.query(Science).filter(Science.id == ident).update({Science.name: form.name})
    db.commit()
    return {"message": "science o'zgartirildi"}


def delete_science(ident, db, carent_user):
    if carent_user.role != "admin":
        return {"message": "siz admin emassiz"}
    db.query(Science).filter(Science.id == ident).delete()
    db.commit()
    return {"message": "science o'chirildi"}