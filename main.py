from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import CountryAnalyser, GpaAnalyser


fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder()
dl = DataLoader('students.csv')
dl.load()
dl.preview()

analysers = [CountryAnalyser(dl.students), GpaAnalyser(dl.students)]
print("-"*30)
print('Running all analysers:')
print("-"*30, "\n")
for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()