import csv
import os
import datetime
from openai import OpenAI
from google.cloud import firestore


def run_keyword_batch(run_id=None, csv_path="data/keywords.csv", limit=None):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    client = OpenAI()
    db = firestore.Client()

    now = datetime.datetime.utcnow()

    if run_id:
        run_ref = db.collection("runs").document(run_id)
    else:
        run_ref = db.collection("runs").document()
        run_id = run_ref.id

    print("Run ID:", run_id)

    run_ref.set({
        "created_at": str(now),
        "provider": "openai",
    })

    print("Runner starting...")
    print(f"Run started at: {now}")
    print("Loading keywords...")

    processed = 0

    with open(csv_path, newline="") as csvfile:
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

            processed += 1
            if limit and processed >= limit:
                break


if __name__ == "__main__":
    run_keyword_batch()
