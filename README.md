# az-cli-utils

A set of simple CLI utilities for managing Azure Key Vault secrets using Python.

## Features
- Upload environment variables as secrets to Azure Key Vault
- Delete secrets from Azure Key Vault

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
poetry run create-az-secrets --vault-name <vault-name> ENV_VAR1 ENV_VAR2 ...
```
- Each ENV_VAR must be set in your environment.
- Secrets will be named as the environment variable, lowercased and with underscores replaced by hyphens.

### Delete secrets from Key Vault

```sh
poetry run delete-az-secrets --vault-name <vault-name> secret-name-1 secret-name-2 ...
```

## Azure Authentication

These utilities use `DefaultAzureCredential` from the Azure SDK. You must be authenticated to Azure (e.g., via `az login` or environment variables such as `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_CLIENT_SECRET`).

See the [Azure Identity documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme) for more details.

