import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests

API_KEY = 'AIzaSyCCkneJqCbQtZrDu3jYi7dJyfybkHI1Xz8'
SIGNUP_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}'
SIGNIN_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}'

# Use a service account.
cred = credentials.Certificate('./serviceCreds.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

signup_payload = {
    'email': 'mpneff19+testthatdb2@gmail.com',
    'password': 'test123',
    'returnSecureToken': True
}
signup_headers = {'content-type': 'application/json'}
r = requests.post(SIGNUP_URL, signup_payload, signup_headers)
rJson = r.json()
if ('error' in rJson):
    print(rJson)
    print("email already exists dummyyyy")
    # Sample output:
    # {'error': {'code': 400, 'message': 'EMAIL_EXISTS', 'errors': [{'message': 'EMAIL_EXISTS', 'domain': 'global', 'reason': 'invalid'}]}}
else:
    print(rJson)
    print("Account created successfully!")
    # Sample output:
    # {'kind': 'identitytoolkit#SignupNewUserResponse', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6IkJrbmtldjQyWm9NMGVwdU1LeTJVd3BJN1ZnQzIiLCJzdWIiOiJCa25rZXY0MlpvTTBlcHVNS3kyVXdwSTdWZ0MyIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTkrdGVzdHRoYXRkYjJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5K3Rlc3R0aGF0ZGIyQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.JCKjax0pzhWSdTkmEs-v2f_YWrtblCwkBER21gUCsdUrrjYxAJ_3FyU29mttAWerqHXkhdexNQqE3xeisMR9vbKKX_yP6L1PamwyGdao-vtgJciuU5WaoNV29XxAoQYJin4K_GtUL6Be8P8eGd1dUJyecoHAm19-CPa2oyE-xAwslH_vvOQTa-XS2t7_ovG4JmbwEVtGEVhGz08C4MClWFwLkbLiMPa2oKGyKE-WSL01eZAWnNHcSsYbyKTzNSHR6wm86eSxTthy9D5JoLgCmOJyK1EGC3ETvhEdLenmxr3eo6Wjf_x9aqxrG7Ee4MBCAiL8FlEnpA8TargXr-rtdw', 'email': 'mpneff19+testthatdb2@gmail.com', 'refreshToken': 'AMf-vBy1W1sOHwkQXjYNp9rDA3zVdF4wot4M1y5WrEEQs97JSJGY-QNbOmX7XCSll21sACziirgmaJa0RaSoRf8i8_ZtIixkRx84vSf2rb2YwgGFQekiouwAzfgmehMkO-LBwI_K7CveVYwufM-cixpRsy6sdSlBrBLUJDIYxAj8Rdiv16u7zUqcDoH9Yk1nB-NdS1T-BFaf74L4cRuXJab0jZ8ZNXqpGzdQWGPeMQXNlvGQLKIOPcM', 'expiresIn': '3600', 'localId': 'Bknkev42ZoM0epuMKy2UwpI7VgC2'}

print("anywayyyyy")

userId = None
signin_payload = {
    'email': 'mpneff19+testthatdb2@gmail.com',
    'password': 'test123',
    'returnSecureToken': True
}
signin_headers = {'content-type': 'application/json'}
r2 = requests.post(SIGNIN_URL, signin_payload, signin_headers)
r2Json = r2.json()
if ('error' in r2Json):
    print(r2Json)
    print("email doesn't exist silly")
    # Sample output:
    # {'error': {'code': 400, 'message': 'INVALID_LOGIN_CREDENTIALS', 'errors': [{'message': 'INVALID_LOGIN_CREDENTIALS', 'domain': 'global', 'reason': 'invalid'}]}}
else:
    print(r2Json)
    userId = r2Json['localId']
    print("Signed in successfully!")
    # Sample output:
    # {'kind': 'identitytoolkit#VerifyPasswordResponse', 'localId': '9wF2J9Mb1XROHJk0u2H4LD4o5Uj1', 'email': 'mpneff19@gmail.com', 'displayName': '', 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdG8tZG8tZGItM2I2ZDYiLCJhdWQiOiJ0by1kby1kYi0zYjZkNiIsImF1dGhfdGltZSI6MTcxMjE2Mzc0NywidXNlcl9pZCI6Ijl3RjJKOU1iMVhST0hKazB1Mkg0TEQ0bzVVajEiLCJzdWIiOiI5d0YySjlNYjFYUk9ISmswdTJINExENG81VWoxIiwiaWF0IjoxNzEyMTYzNzQ3LCJleHAiOjE3MTIxNjczNDcsImVtYWlsIjoibXBuZWZmMTlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1wbmVmZjE5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.gejE0ts69BX_5omnj9uv-2Gu3ULG38hjRxQxblCeFVQnAgkaddFNnIYxhIEDrxO0ooGj_VBer9koeCl-KaUM_0HQr27yWL4aZmR-1vS9ii9IQZ6S7X2ll-F9fGgNoLdKdgN9ezBuUkWGqF4TwNqYfY8xJG6znkyqanb2v7HLbjiWteyUYCu1bxGJJFYK6jr9_ediqo9lcyL25-synGvOGiivdxJlbSsVlIVJF0cQFz2rJmOkatpV1eyar5Akz8Imw4Y9A9sN8fk-_vGuomFwP76wi9KJXTv8ACQlQsHX1LKFpmkcBiRvc9yGSSLAexRwa0qmUpJo6HK_3ENvonAuNg', 'registered': True, 'refreshToken': 'AMf-vBxsJcoXg9LCUV2-KXg2Tpy7Wb4RGIU6PW1kPIN5f6TI9hzIempWsxHQnZp-cPkH10gOaY6q0YcXOxDmOnvipAzZzNN2UwQ1UXOSjdYGe53GCT5md8Bo4QZ4qde4Ar4gEd5KnB3g47J5HpolrXeCfIMo1KxzkMWCdTZPNvukYVXcbz3J5YpsmApTpMsLmsqziskT53QW71aiSsLNfB3Gb9jrSaiDUg', 'expiresIn': '3600'}


doc_ref = db.collection("todoitems").document(userId)
iterate_ref = doc_ref.collection("todos").list_documents()
item_ref = doc_ref.collection("todos").document()
item_ref.set({"title": "test item", "completed": False})
# update_data = {"duedate": firestore.DELETE_FIELD}
update_data = {"completed": True}

i = 0
for doc in iterate_ref:
    if i == 4:
        doc.update(update_data)
    print(f"{doc.id} => {doc.get().to_dict()}")
    if i == 2:
        doc.delete()
        i += 1
        print(f"<!-- {doc.id} DELETED --!>")
    i += 1

# doc_ref = db.collection("users").document("aturing")
# doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})