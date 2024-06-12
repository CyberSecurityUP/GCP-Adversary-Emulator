import subprocess

def run_cleanup_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Successfully executed: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute: {command}")
        print(e.stderr)
        return None

def cleanup():
    print("Cleaning up the environment...")

    # List of cleanup commands
    cleanup_commands = [
        "gcloud compute instances delete instance-name --quiet",
        "gcloud logging sinks delete my-sink --quiet",
        "gcloud logging logs delete my-log --quiet",
        "gcloud projects remove-iam-policy-binding [PROJECT_ID] --member='user:attacker@example.com' --role='roles/editor' --quiet",
        "gcloud projects remove-iam-policy-binding [PROJECT_ID] --member='serviceAccount:service-account@project.iam.gserviceaccount.com' --role='roles/owner' --quiet",
        "gcloud compute snapshots delete stolen-snapshot --quiet",
        "gcloud compute images delete stolen-image --quiet",
        "gcloud deployment-manager deployments delete deployment-name --quiet",
        "gcloud functions delete function-name --quiet",
        "gcloud projects remove-iam-policy-binding [PROJECT_ID] --member='user:[USER_EMAIL]' --role='roles/[ROLE_NAME]' --quiet",
        "gcloud compute instances reset instance-name --quiet",
        "gcloud compute instances set-machine-type instance-name --machine-type n1-standard-1 --quiet",
        "gcloud compute disks delete stolen-snapshot --quiet",
        "gcloud compute disks delete stolen-image --quiet"
    ]

    # Execute each cleanup command
    for command in cleanup_commands:
        run_cleanup_command(command)

    print("Cleanup completed.")

if __name__ == "__main__":
    cleanup()
