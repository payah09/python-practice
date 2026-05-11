import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding="utf-8") as f:
                self.students = list(csv.DictReader(f))
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return
    def preview(self, n = 5):
        print(f"First {n} rows:")
        print("-"*30)
        for i in range(n):
            print(self.students[i]["student_id"], self.students[i]["age"], self.students[i]["gender"], self.students[i]["country"], self.students[i]["GPA"], sep=" | ")
        print("-"*30)