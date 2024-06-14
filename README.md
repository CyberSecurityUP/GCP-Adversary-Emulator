# GCP Adversary Emulator

GCP Adversary Emulator is an adversary emulation tool designed for performing security tests on Google Cloud Platform (GCP) environments. It allows the simulation of various adversary tactics, techniques, and procedures (TTPs), providing a robust approach to testing your systems' resilience.

## Features

- GCP Authentication
- Tactics and Techniques Selection
- Custom Command Execution
- HTML Report Generation
- Environment Cleanup after Tests
- Support for multiple tactics such as Reconnaissance, Initial Access, Execution, Privilege Escalation, Persistence, Exfiltration, Defense Evasion, Credential Access, Lateral Movement, and Collection

## Installation

### Requirements

- Python 3.x
- `gcloud` CLI installed and configured
- Appropriate permissions in GCP to execute commands

### Steps

1. Clone the repository:

```bash
git clone https://github.com/CyberSecurityUP/GCP-Adversary-Emulator
cd GCP-Adversary-Emulator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the tool:

```bash
python main.py
```

2. Follow the terminal instructions to authenticate with GCP, select tactics and techniques, and view the report.

### Command Examples

- **GCP Authentication**: Activate authentication using a service account.
- **Select Tactics and Techniques**: Choose from a variety of tactics and techniques.
- **Generate Report**: Enable report generation with the `--report-enable` flag.

```bash
python main.py --report-enable
```

## File Structure

- `main.py`: Main script that initializes the tool.
- `modules/`: Contains specific function modules.
  - `authenticate.py`: GCP authentication function.
  - `cleanup.py`: Environment cleanup function.
  - `display_ttp.py`: Display tactics and techniques.
  - `execute_technique.py`: Execute techniques.
  - `load_ttps.py`: Load TTPs JSON.
  - `report.py`: Report generation.
- `scripts/`: Additional scripts used for emulation.

## Additional Tools

To complement your security testing on GCP, consider using the following tools:

- [GCP IAM Privilege Escalation](https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/tree/master): Tools and techniques for privilege escalation on GCP.
- [k8senumeration](https://github.com/CyberSecurityUP/k8senumeration): Tool for enumerating Kubernetes clusters.
- [gcp_enum](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/gcp_enum): Enumeration scripts for GCP.
- [GCPBucketBrute](https://github.com/RhinoSecurityLabs/GCPBucketBrute): Brute force tool for GCP buckets.

### Future Release

In our next release, we plan to expand the capabilities of GCPAdversary to focus on Google Kubernetes Engine (GKE) and other Kubernetes environments within GCP. This update will include:

- Enhanced TTPs specific to Kubernetes clusters.
- Integration with common Kubernetes tools and frameworks.
- Advanced techniques for testing Kubernetes security.
- Automated scanning and exploitation of Kubernetes vulnerabilities.

Stay tuned for more updates and features as we continue to enhance GCPA dversary Emulator to meet the evolving needs of cloud security testing.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

Sure! Here's an updated README with a section on how to add TTPs to the JSON and `execute_technique.py`, along with step-by-step instructions:

---

### Adding TTPs to JSON

1. Open the `ttps/ttps.json` file.
2. Locate the appropriate section for the tactic you want to add a technique to.
3. Add a new JSON object with the `id`, `details`, and `command` fields. For example:

```json
{
    "GCP": {
        "Reconnaissance": [
            {
                "id": "T1590-1",
                "details": "Gathering GCP resources",
                "command": "gcloud compute instances list"
            },
            {
                "id": "T1590-2",
                "details": "Analyzing gcloud configuration",
                "command": "gcloud info --quiet; gcloud config list --quiet; gcloud auth list --quiet"
            }
            // Add your new TTP here
        ]
        // Other tactics...
    }
}
```

### Updating `execute_technique.py`

1. Open the `modules/execute_technique.py` file.
2. Ensure that the command placeholders in the new TTP are supported by the input prompts. If necessary, add new input prompts for any placeholders not currently handled.
3. For example, if your new command includes a placeholder `<new_placeholder>`, add:

```python
if "<new_placeholder>" in command:
    new_value = input("Enter the new value for <new_placeholder>: ")
    command = command.replace("<new_placeholder>", new_value)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
