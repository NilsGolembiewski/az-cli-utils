import click
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import sys

@click.command()
@click.option('--vault-name', '-v', required=True, help='Name of the Azure Key Vault.')
@click.option('--secret-name', '-s', required=True, help='Name of the secret to create or update.')
@click.option('--file', '-f', required=True, type=click.Path(exists=True, dir_okay=False), help='Path to the file whose contents will be stored as the secret value.')
def main(vault_name, secret_name, file_path):
    """Create or update a secret in Azure Key Vault with the contents of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            secret_value = f.read()
    except Exception as e:
        click.echo(f"Error reading file: {e}", err=True)
        sys.exit(1)

    kv_url = f"https://{vault_name}.vault.azure.net/"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_url, credential=credential)

    try:
        client.set_secret(secret_name, secret_value)
        click.echo(f"Secret '{secret_name}' set in vault '{vault_name}' from file '{file_path}'.")
    except Exception as e:
        click.echo(f"Error setting secret: {e}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main() 
