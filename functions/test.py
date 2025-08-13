from models.lesson import Lesson
from models.test import Test


def create_test(form, db, current_user):
    if current_user.role != "admin":
        return {"message": "siz admin emassiz"}
    if not db.query(Lesson).filter(Lesson.id == form.lessone_id).first():
        return {"message": "bunfay science mavjud emas"}
    test = Test(name=form.name,
                question=form.question,
                options=form.options,
                answer=form.answer,
                explanation=form.explanation,
                level=form.level,
                lesson_id=form.lessone_id)
    db.add(test)
    db.commit()
    return {"message": "test yaratildi"}


def update_test(ident, form, db, current_user):
    if current_user.role != "admin":
        return {"message": "siz admin emassiz"}
    if not db.query(Lesson).filter(Lesson.id == form.lessone_id).first():
        return {"message": "bunfay science mavjud emas"}
    db.query(Test).filter(Test.id == ident).update({Test.name: form.name,
                                                   Test.question: form.question,
                                                   Test.options: form.options,
                                                   Test.answer: form.answer,
                                                   Test.explanation: form.explanation,
                                                   Test.level: form.level,
                                                   })
    db.commit()
    return {"message": "test o'zgartirildi"}


def delete_test(ident, db, current_user):
    if current_user.role != "admin":
        return {"message": "siz admin emassiz"}
    db.query(Test).filter(Test.id == ident).delete()
    db.commit()
    return {"message": "test o'chirildi"}