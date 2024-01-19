from sqlalchemy import select

from app.models import User


def test_create_user_model(session):
    user = User(username='John2', password='seila', email='jonh@gmail.com')
    session.add(user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'John2'))

    assert user.username == 'John2'
    assert user.email == 'jonh@gmail.com'
