import csv
import datetime
from openai import OpenAI

client = OpenAI()

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

        print("Keyword:", keyword)
        print("Prompt:", prompt)
        print("Response:", response.output_text)
        print("---")