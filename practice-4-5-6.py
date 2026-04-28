import os, csv, json
#task B1
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    def check_file(self):
        print("Checking file...")
        file_exists = os.path.exists(self.filename)
        if file_exists:
            print(f"File found: {self.filename} ")
            return file_exists
        print(f"Error: {self.filename} not found. Please download the file from LMS.")
        return file_exists
    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created output folder: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

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

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self):
        country_counts = {}
        for row in self.students:
            country = row["country"]
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1
        top_3 = sorted(country_counts.items(), key= lambda x: x[1], reverse=True)[:3]
        self.result = {
        "total_countries": len(country_counts),
        "top_3": top_3,
        "country_counts": country_counts}
        return self.result
    def print_results(self):
        print("-"*30)
        print("Country Analysis")
        print("-"*30)
        print(f"Total countries : {self.result['total_countries']}")
        print("Top 3 Countries:")
        i = 1
        for country, count in self.result["top_3"]:
            print(f"{i}. {country}: {count}")
            i += 1
        print("-"*30)

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, mode='w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Could not write to a file. {e}")


#main
fm = FileManager('students.csv')
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()
dl = DataLoader('students.csv')
dl.load()
dl.preview()
analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()
saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()