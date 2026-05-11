class DataAnalyser():
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self):
        print("Not implemented — use a child class")
    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")
    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)
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
        "total_students": len(self.students),
        "total_countries": len(country_counts),
        "top_3": top_3,
        "all_countries": country_counts}
        return self.result
    def print_results(self):
        print("="*30)
        print("COUNTRY ANALYSIS REPORT")
        print("="*30)
        super().print_results()
        print("="*30, "\n")
    def __str__(self):
        return f"CountryAnalyser: Country Statistics, {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)
    def analyse(self):
        gpas = []
        high_performer_count = 0
        for student in self.students:
            try:
                gpa_value = float(student['GPA']) 
                gpas.append(gpa_value)
                if gpa_value > 3.5:
                    high_performer_count += 1
            except (ValueError):
                print(f"Warning: could not convert value for student {student['student_id']} — skipping row.")
                continue
        avg_gpa = sum(gpas) / len(gpas)
        max_gpa = max(gpas)
        min_gpa = min(gpas)
        self.result = {
            "total_students": len(gpas),
            "average_gpa": round(avg_gpa, 2),
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_performer_count
        }
        return self.result
    def print_results(self):
        print("="*30)
        print("GPA ANALYSIS REPORT")
        print("="*30)
        super().print_results()
        print("="*30, "\n")
    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"