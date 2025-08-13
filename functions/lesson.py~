from models.lesson import Lesson
from utils.icon import upload_icon


def create_lesson(name, icon, science_id, db, current_user):
    if current_user.role != 'admin':
        return {'message': 'siz admin emassiz'}
    icon_name = upload_icon(icon)
    lesson = Lesson(name=name,
                    icon=icon_name,
                    science_id=science_id,)
    db.add(lesson)
    db.commit()
    return {'message': 'lesson yaratildi'}


def update_lesson(ident, name, icon, science_id, db, current_user):
    if current_user.role != 'admin':
        return {'message': 'siz admin emassiz'}
    db.query(Lesson).filter(Lesson.id == ident).update({Lesson.name: name,
                                                        Lesson.icon: upload_icon(icon),
                                                        Lesson.science_id: science_id,
                                                        })
    db.commit()
    return {'message': "lesson o'zgartirildi"}


def delete_lesson(ident, db, current_user):
    if current_user.role != 'admin':
        return {'message': 'siz admin emassiz'}
    db.query(Lesson).filter(Lesson.id == ident).delete()
    db.commit()
    return {'message': "lesson o'chirildi"}