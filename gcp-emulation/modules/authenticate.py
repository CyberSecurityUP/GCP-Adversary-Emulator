import os
import subprocess

def authenticate_gcp():
    print("GCP Authentication Options:")
    print("1. Authenticate with credentials file")
    print("2. Authenticate without credentials file")
    choice = input("Enter your choice: ")

    if choice == "1":
        credential_path = input("Enter the path to your GCP credentials file: ")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
        command = f"gcloud auth login --login-config={credential_path}"
    elif choice == "2":
        command = "gcloud auth login"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    try:
        print(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True)
        print("Authentication successful.")
    except subprocess.CalledProcessError as e:
        print("Authentication failed.")
        print(e.stderr)
