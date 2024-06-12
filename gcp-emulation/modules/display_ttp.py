from modules.execute_technique import execute_technique

def display_ttp_options(ttp_structure, report=None):
    while True:
        print("Select a category:")
        categories = list(ttp_structure.keys())
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category}")
        print("0. Go back")

        category_choice = input("Enter your choice: ")

        if category_choice == "0":
            return
        else:
            try:
                category_choice = int(category_choice) - 1
                category_name = categories[category_choice]
                display_tactics(ttp_structure, category_name, report)
            except (IndexError, ValueError):
                print("Invalid choice, please try again.")

def display_tactics(ttp_structure, category_name, report=None):
    while True:
        print(f"\nTactics under {category_name}:")
        tactics = ttp_structure[category_name]
        for idx, tactic in enumerate(tactics.keys()):
            print(f"{idx + 1}. {tactic}")
        print("0. Go back")

        tactic_choice = input("Enter your choice: ")

        if tactic_choice == "0":
            return
        else:
            try:
                tactic_choice = int(tactic_choice) - 1
                tactic_name = list(tactics.keys())[tactic_choice]
                display_techniques(ttp_structure, category_name, tactic_name, report)
            except (IndexError, ValueError):
                print("Invalid choice, please try again.")

def display_techniques(ttp_structure, category_name, tactic_name, report=None):
    while True:
        techniques = ttp_structure[category_name][tactic_name]
        print(f"\nTechniques under {category_name} - {tactic_name}:")
        for idx, technique in enumerate(techniques):
            print(f"{idx + 1}. {technique['id']}: {technique['details']}")
        print("00. Execute all techniques")
        print("0. Go back")

        technique_choice = input("Enter your choice: ")

        if technique_choice == "0":
            return
        elif technique_choice == "00":
            for technique in techniques:
                try:
                    execute_technique(technique, category_name, tactic_name, report)
                except KeyboardInterrupt:
                    print("\nExecution skipped by user.")
                    if report:
                        report.add_result(category_name, tactic_name, technique["id"], "Skipped", "Execution skipped by user.")
                    continue
        else:
            try:
                technique_choice = int(technique_choice) - 1
                selected_technique = techniques[technique_choice]
                try:
                    execute_technique(selected_technique, category_name, tactic_name, report)
                except KeyboardInterrupt:
                    print("\nExecution skipped by user.")
                    if report:
                        report.add_result(category_name, tactic_name, selected_technique["id"], "Skipped", "Execution skipped by user.")
            except (IndexError, ValueError):
                print("Invalid choice, please try again.")
