from models import user
from database.firestore_connection import firestore_db
from database.models import db_user_model


def create_user(user:  user.UserCreate):
    data = db_user_model.DB_User(
        first=user.first, last=user.last, born=user.born, middle=user.middle, email=user.email)

    # get the id before adding the data
    new_user_ref = firestore_db.collection('users').document()
    # print(new_user_ref.id)

    new_user_ref.set(data.get_data())
    data_dict = data.get_data()
    data_dict['id'] = new_user_ref.id
    # print(data_dict)
    return data_dict


def get_user_by_email(email: str):
    existing_email = firestore_db.collection('users').where(
        'email', '==', f'{email}').get()
    email: str = None
    for email in existing_email:
        user_dict = email.to_dict()
        email = user_dict['email']

    return email


def get_users():
    users = firestore_db.collection('users').stream()
    user_array = []
    for user in users:
        _user = user.to_dict()
        _user['id'] = user.id
        user_array.append(_user)

    # print(user_array)
    return user_array
