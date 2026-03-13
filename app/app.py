from flask import Flask
from google.cloud import firestore

app = Flask(__name__)

db = firestore.Client()

@app.route("/")
def home():
    doc_ref = db.collection("runs").document()
    doc_ref.set({
        "message": "first firestore write",
    })

    return "Wrote to Firestore"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)