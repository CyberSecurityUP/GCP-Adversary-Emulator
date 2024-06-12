import subprocess

def execute_technique(technique, category, tactic, report=None):
    command = technique["command"]

    if "instance-name" in command:
        instance_name = input("Enter the instance name: ")
        command = command.replace("instance-name", instance_name)
    if "key-file" in command:
        key_file = input("Enter the path to your key file: ")
        command = command.replace("<KEY_FILE>", key_file)
    if "token" in command:
        token = input("Enter the token: ")
        command = command.replace("<TOKEN>", token)
    if "project" in command:
        project_id = input("Enter the project ID: ")
        command = command.replace("<PROJECT_ID>", project_id)
    if "function" in command:
        function_name = input("Enter the function name: ")
        command = command.replace("<FUNCTION_NAME>", function_name)
    if "account-name" in command:
        account_name = input("Enter the account name: ")
        command = command.replace("<ACCOUNT_NAME>", account_name)
    if "role-name" in command:
        role_name = input("Enter the role name: ")
        command = command.replace("<ROLE_NAME>", role_name)
    if "permissions" in command:
        permissions = input("Enter the permissions: ")
        command = command.replace("<PERMISSIONS>", permissions)
    if "policy" in command:
        policy = input("Enter the policy: ")
        command = command.replace("<POLICY>", policy)
    if "service-name" in command:
        service_name = input("Enter the service name: ")
        command = command.replace("<SERVICE_NAME>", service_name)
    if "image" in command:
        image = input("Enter the image: ")
        command = command.replace("<IMAGE>", image)
    if "service-account" in command:
        service_account = input("Enter the service account: ")
        command = command.replace("<SERVICE_ACCOUNT>", service_account)
    if "trigger-id" in command:
        trigger_id = input("Enter the trigger ID: ")
        command = command.replace("<TRIGGER_ID>", trigger_id)
    if "repo-name" in command:
        repo_name = input("Enter the repo name: ")
        command = command.replace("<REPO_NAME>", repo_name)
    if "branch-name" in command:
        branch_name = input("Enter the branch name: ")
        command = command.replace("<BRANCH_NAME>", branch_name)
    if "<victim-project>" in command:
        victim_project = input("Enter the victim project: ")
        command = command.replace("<victim-project>", victim_project)
    if "<zone>" in command:
        zone = input("Enter the zone: ")
        command = command.replace("<zone>", zone)
    if "<victim-disk>" in command:
        victim_disk = input("Enter the victim disk: ")
        command = command.replace("<victim-disk>", victim_disk)
    if "<email attack>" in command:
        email_attack = input("Enter the attacker email: ")
        command = command.replace("<email attack>", email_attack)
    if "[USER_EMAIL]" in command:
        user_email = input("Enter the user email: ")
        command = command.replace("[USER_EMAIL]", user_email)
    if "<command>" in command:
        custom_command = input("Enter the command to execute: ")
        command = command.replace("<command>", custom_command)
    if "[PROJECT_ID]" in command:
        project_id = input("Enter the project ID: ")
        command = command.replace("[PROJECT_ID]", project_id)
    if "[SECRET_NAME]" in command:
        secret_name = input("Enter the secret name: ")
        command = command.replace("[SECRET_NAME]", secret_name)
    if "[BUCKET_NAME]" in command:
        bucket_name = input("Enter the bucket name: ")
        command = command.replace("[BUCKET_NAME]", bucket_name)

    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("Result: Positive")
        print(result.stdout)
        if report:
            report.add_result(category, tactic, technique["id"], "Positive", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Result: Failed")
        print(e.stderr)
        if report:
            report.add_result(category, tactic, technique["id"], "Failed", e.stderr)
    except KeyboardInterrupt:
        print("\nExecution skipped by user.")
        if report:
            report.add_result(category, tactic, technique["id"], "Skipped", "Execution skipped by user.")
