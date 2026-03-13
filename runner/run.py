import csv
import datetime

print("Runner starting...")

now = datetime.datetime.utcnow()
print(f"Run started at: {now}")

print("Loading keywords...")

with open("data/keywords.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("Keyword:", row["keyword"])