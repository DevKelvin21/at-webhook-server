import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("./at-logic-flow-dev-firebase-adminsdk-4onlh-aa6e2aee4a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def main(payload: dict, id: str):
    db.collection(u'request').document(id).set(payload)