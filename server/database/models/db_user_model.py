# firestore_db.collection(u'users').document(u'mjoe').set(
#     {'born': 1921, 'first': 'Joe', 'last': 'Mark', 'middle': 'Tom'})

from typing import Optional


class DB_User():
    def __init__(self, first: str, last: str, born: int, email: str, middle: Optional[str] = None):

        self.first = first
        self.last = last
        self.born = born
        self.middle = middle
        self.email = email

    def get_data(self) -> dict:
        return {
            'first': self.first,
            'last': self.last,
            'born': self.born,
            'middle': self.middle,
            'email': self.email
        }
