from models.result import Result
from models.test import Test
from models.users import Users


def create_result(form, db, current_user):
    if not db.query(Test).filter(Test.id == form.test_id).first():
        return {"message": "bunday test mavjud emas"}
    user = db.query(Users).filter(Users.id == current_user.id).first()
    test = db.query(Test).filter(Test.id == form.test_id).first()
    if test.answer != form.answer:
        answer = "noto'gri"
    else:
        answer = "to'gri"
        if test.level == "easy":
            user.balans += 10
        elif test.level == "medium":
            user.balans += 20
        elif test.level == "hard":
            user.balans += 30

    result = Result(
        test_id=form.test_id,
        answer=answer,
        user_id=current_user.id
    )
    db.add(result)
    db.commit()
