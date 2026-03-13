import csv
import datetime
from openai import OpenAI
from google.cloud import firestore

client = OpenAI()
db = firestore.Client()

now = datetime.datetime.utcnow()

run_ref = db.collection("runs").document()
run_id = run_ref.id

print("Run ID:", run_id)

run_ref.set({
    "created_at": str(now),
    "provider": "openai",
})

print("Run ID:", run_id)

print("Runner starting...")

now = datetime.datetime.utcnow()
print(f"Run started at: {now}")

print("Loading keywords...")

with open("data/keywords.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        keyword = row["keyword"]
        prompt = f"What does AI say about: {keyword}?"

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        run_ref.collection("results").document().set({
            "keyword": keyword,
            "prompt": prompt,
            "response": response.output_text,
            "created_at": str(now),
        })

        print("Keyword:", keyword)
        print("Prompt:", prompt)
        print("Response:", response.output_text)
        print("---")