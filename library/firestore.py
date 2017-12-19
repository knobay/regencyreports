"""Functions for doing stuff in firestore"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def saveissues(jsondata, cert):
    "Save json issues to fire store"
    # Use a service account
    cred = credentials.Certificate(cert)
    firebase_admin.initialize_app(cred)
    dstore = firestore.client()

    for doc in jsondata:
        doc_ref = dstore.collection('issues').document(doc['id'])
        doc_ref.set({
            'updated': doc['updated'],
            'summary': doc['summary'],
            'description': doc['description'],
            'status': doc['status'],
            'assignee': doc['assignee'],
            'creator': doc['creator'],
            'created': doc['created'],
            'url': doc['url'],
            })
