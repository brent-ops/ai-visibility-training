import csv
import datetime

print("Runner starting...")

now = datetime.datetime.utcnow()
print(f"Run started at: {now}")

print("Loading keywords...")

with open("data/keywords.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        keyword = row["keyword"]

        prompt = f"What does AI say about: {keyword}?"

        print("Keyword:", keyword)
        print("Prompt:", prompt)
        print("---")