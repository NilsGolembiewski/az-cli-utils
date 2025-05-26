import sys
import click
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

@click.command()
@click.option('--vault-name', '-v', prompt=True, help='Azure Key Vault name (without https://)')
@click.argument('secrets', nargs=-1)
def main(vault_name, secrets):
    """
    Deletes the given SECRETS from the specified Azure Key Vault.
    """
    if not secrets:
        print("No secrets specified. Provide at least one as an argument.")
        sys.exit(1)

    vault_url = f"https://{vault_name}.vault.azure.net/"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    for secret_name in secrets:
        try:
            poller = client.begin_delete_secret(secret_name)
            deleted_secret = poller.result()
            print(f"Deleted secret: {secret_name}")
        except Exception as e:
            print(f"Failed to delete secret '{secret_name}': {e}")

if __name__ == "__main__":
    main() 
