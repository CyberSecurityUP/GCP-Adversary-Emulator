import argparse
from modules.authenticate import authenticate_gcp
from modules.cleanup import cleanup
from modules.display_ttp import display_ttp_options
from modules.load_ttps import load_ttps
from modules.report import Report

# Carregar os TTPs do arquivo JSON
ttp_structure = load_ttps('ttps/ttps.json')

def main():
    parser = argparse.ArgumentParser(description="Adversary Emulation Tool for GCP and Kubernetes")
    parser.add_argument('--report-enable', action='store_true', help='Enable report generation')
    args = parser.parse_args()

    report = Report() if args.report_enable else None

    while True:
        print("\nAdversary Emulation Tool for GCP and Kubernetes")
        print("1. Authenticate GCP")
        print("2. Select Tactics and Techniques")
        print("3. Cleanup")
        if args.report_enable:
            print("4. Display Report")
            print("5. Exit")
        else:
            print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            authenticate_gcp()
        elif choice == "2":
            display_ttp_options(ttp_structure, report)
        elif choice == "3":
            cleanup()
        elif choice == "4" and args.report_enable:
            report.display_cli_report()
        elif choice == "4" or (choice == "5" and args.report_enable):
            if report:
                report.generate_html_report('reports')
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()