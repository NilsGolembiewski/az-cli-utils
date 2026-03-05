# az-cli-utils

A set of simple CLI utilities for managing Azure Key Vault and Storage Account resources using Python.

## Features
- Upload environment variables as secrets to Azure Key Vault
- Delete secrets from Azure Key Vault
- Whitelist current public IP for Azure Storage Accounts

## Installation

This project requires Python 3.10–3.13.

Install with Poetry:

```sh
poetry install
```

Or with pip:

```sh
pip install .
```

## Usage

### Upload environment variables as secrets

```sh
poetry run az-secrets-create --vault-name <vault-name> ENV_VAR1 ENV_VAR2 ...
```
- Each ENV_VAR must be set in your environment.
- Secrets will be named as the environment variable, lowercased and with underscores replaced by hyphens.

### Delete secrets from Key Vault

```sh
poetry run az-secrets-delete --vault-name <vault-name> secret-name-1 secret-name-2 ...
```

### Whitelist public IP for Azure Storage

```sh
poetry run az-storage-whitelist-ip --resource-group <resource-group> --account-name <storage-account-name>
```
- Fetches your current public IPv4 address and adds it to the storage account's network rule whitelist.
- Uses `az` CLI under the hood. Make sure it's installed and you're authenticated.

## Azure Authentication

These utilities use `DefaultAzureCredential` from the Azure SDK. You must be authenticated to Azure (e.g., via `az login` or environment variables such as `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_CLIENT_SECRET`).

See the [Azure Identity documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme) for more details.

