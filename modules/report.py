import os
from datetime import datetime
from prettytable import PrettyTable

class Report:
    def __init__(self):
        self.results = []

    def add_result(self, category, tactic, technique, result, output):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = "reports/outputs"
        output_file = f"{technique}_{timestamp}.txt"
        output_path = os.path.join(output_dir, output_file)
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        with open(output_path, 'w') as file:
            file.write(output)
        
        self.results.append({
            "category": category,
            "tactic": tactic,
            "technique": technique,
            "result": result,
            "output_file": output_path
        })

    def generate_html_report(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(directory, f"report_{timestamp}.html")

        html_content = "<html><head><title>Adversary Emulation Report</title></head><body>"
        html_content += "<h1>Adversary Emulation Report</h1><table border='1'><tr><th>Category</th><th>Tactic</th><th>Technique</th><th>Result</th></tr>"

        for result in self.results:
            relative_output_path = os.path.relpath(result['output_file'], directory)
            html_content += f"<tr><td>{result['category']}</td><td>{result['tactic']}</td><td><a href='{relative_output_path}' target='_blank'>{result['technique']}</a></td><td>{result['result']}</td></tr>"

        html_content += "</table></body></html>"

        with open(file_path, 'w') as file:
            file.write(html_content)

        print(f"Report saved to {file_path}")

    def display_cli_report(self):
        table = PrettyTable()
        table.field_names = ["Category", "Tactic", "Technique", "Result"]

        for result in self.results:
            table.add_row([result['category'], result['tactic'], result['technique'], result['result']])

        print(table)
