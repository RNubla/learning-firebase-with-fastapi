
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firestore_db = firestore.client()

# firestore_db.collection(u'users').document(u'mjoe').set(
#     {'born': 1921, 'first': 'Joe', 'last': 'Mark', 'middle': 'Tom'})
