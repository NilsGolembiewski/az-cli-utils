import subprocess
import requests
import sys
import shutil
import click


def get_public_ip():
    """Fetches the current public IPv4 address."""
    try:
        response = requests.get("https://api.ipify.org", timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        sys.exit(1)


def run_az_command(command):
    """Executes an Azure CLI command and returns the result."""
    if not shutil.which("az"):
        print("Error: 'az' CLI is not installed or not in PATH.")
        sys.exit(1)

    try:
        print(f"Executing: {' '.join(command)}")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing az command: {e.stderr}")
        sys.exit(1)


@click.command()
@click.option(
    "--resource-group",
    "-g",
    required=True,
    help="Name of the resource group.",
)
@click.option(
    "--account-name",
    "-n",
    required=True,
    help="Name of the storage account.",
)
def main(resource_group, account_name):
    """
    Adds current public IP to Azure Storage Account whitelist.
    """
    print("Fetching current public IP...")
    current_ip = get_public_ip()
    print(f"Current public IP: {current_ip}")

    # Construct the az command
    command = [
        "az",
        "storage",
        "account",
        "network-rule",
        "add",
        "--resource-group",
        resource_group,
        "--account-name",
        account_name,
        "--ip-address",
        current_ip,
    ]

    print(f"Adding {current_ip} to whitelist for storage account '{account_name}'...")
    run_az_command(command)
    print("Successfully added IP to whitelist.")

    print(
        "\nNote: Ensure your storage account's default network access is set to 'Deny' for the whitelist to take effect."
    )
    print(
        f"You can do this with: az storage account update -g {resource_group} -n {account_name} --default-action Deny"
    )


if __name__ == "__main__":
    main()
