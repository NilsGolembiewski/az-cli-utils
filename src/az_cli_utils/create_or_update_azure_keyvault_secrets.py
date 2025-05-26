import os
import sys
import click
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

@click.command()
@click.option('--vault-name', '-v', prompt=True, help='Azure Key Vault name (without https://)')
@click.argument('env_vars', nargs=-1)
def main(vault_name, env_vars):
    """
    Uploads the values of the given ENV_VARS as secrets to the specified Azure Key Vault.
    The secret name will be the env var name lowercased and with underscores replaced by hyphens.
    """
    if not env_vars:
        print("No environment variables specified. Provide at least one as an argument.")
        sys.exit(1)

    vault_url = f"https://{vault_name}.vault.azure.net/"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    for env_var in env_vars:
        value = os.environ.get(env_var)
        if value is None:
            print(f"Environment variable '{env_var}' is not set. Skipping.")
            continue
        secret_name = env_var.lower().replace('_', '-')
        try:
            client.set_secret(secret_name, value)
            print(f"Set secret: {secret_name} (from env var: {env_var})")
        except Exception as e:
            print(f"Failed to set secret '{secret_name}': {e}")

if __name__ == "__main__":
    main() 
