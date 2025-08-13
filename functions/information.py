from models.information import Information
from models.lesson import Lesson
from utils.icon import upload_image


def create_information(description, example, lesson_id, db, current_user):
    if current_user.role != 'admin':
        return {'message': 'siz admin emassiz'}
    new_example = upload_image(example)
    if not db.query(Lesson).filter(Lesson.id == lesson_id).first():
        return {"message": "bunfay lesson mavjud emas"}
    information = Information(description=description,
                              example=new_example,
                              lesson_id=lesson_id
                              )
    db.add(information)
    db.commit()
    return {'message': 'information yaratildi'}


def update_information(ident, description, example, lesson_id, db, current_user):
    if current_user.role != 'admin':
        return {'message': 'siz admin emassiz'}
    if not db.query(Lesson).filter(Lesson.id == lesson_id).first():
        return {"message": "bunfay lesson mavjud emas"}
    db.query(Information).filter(Information.id == ident).update({Information.description: description,
                                                                  Information.example: upload_image(example),
                                                                  Information.lesson_id: lesson_id,
                                                                  })
    db.commit()
    return {'message': "information o'zgartirildi"}


def delete_information(ident, db, current_user):
    if current_user.role != 'admin':
        return {'message': 'siz admin emassiz'}
    db.query(Information).filter(Information.id == ident).delete()
    db.commit()
    return {'message': "information o'chirildi"}
