import os

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
        exit()
        return file_exists
    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created output folder: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")