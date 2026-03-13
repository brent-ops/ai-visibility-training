import csv
import datetime
from openai import OpenAI
from google.cloud import firestore

client = OpenAI()
db = firestore.Client()

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
        db.collection("runner_results").document().set({
    "keyword": keyword,
    "prompt": prompt,
    "response": response.output_text,
    "created_at": str(now),
})

        print("Keyword:", keyword)
        print("Prompt:", prompt)
        print("Response:", response.output_text)
        print("---")