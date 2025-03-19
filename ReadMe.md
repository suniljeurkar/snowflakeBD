# SnowflakeBD

**SnowflakeBD** is a Python-based project designed to perform data validation and integrity checks on Snowflake databases. The project leverages the Snowflake Python Connector and utilizes RSA key pair authentication for secure connections.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Dependencies](#2-install-dependencies)
  - [3. Generate RSA Key Pair using OpenSSL](#3-generate-rsa-key-pair-using-openssl)
  - [4. Configure Snowflake User with Public Key](#4-configure-snowflake-user-with-public-key)
  - [5. Set Environment Variables](#5-set-environment-variables)
  - [6. Run Tests](#6-run-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Data Integrity Tests**: Ensures the consistency and accuracy of data within Snowflake tables.
- **Business Logic Validation**: Validates that business rules and constraints are correctly enforced in the database.
- **Performance Testing**: Monitors and reports on query performance to identify potential bottlenecks.
- **API vs Database Consistency**: Compares data between APIs and the Snowflake database to ensure synchronization.

## Prerequisites

- **Python 3.6 or higher**: Ensure Python is installed on your system.
- **Snowflake Account**: Access to a Snowflake account with appropriate permissions.
- **OpenSSL**: Required for generating RSA key pairs.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/suniljeurkar/snowflakeBD.git
cd snowflakeBD
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Generate RSA Key Pair using OpenSSL

For secure authentication, generate an RSA key pair:

1. **Generate a 2048-bit RSA Private Key**:

   ```bash
   openssl genrsa -out rsa_key.pem 2048
   ```

2. **Convert Private Key to PKCS#8 Format**:

   ```bash
   openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in rsa_key.pem -out rsa_key.p8
   ```

3. **Extract the Public Key**:

   ```bash
   openssl rsa -in rsa_key.pem -pubout -out rsa_key.pub
   ```

   Ensure the public key starts with `-----BEGIN PUBLIC KEY-----`.

**Note**: Keep your private key (`rsa_key.p8`) secure and do not share it.

### 4. Configure Snowflake User with Public Key

Assign the public key to your Snowflake user:

1. Open the `rsa_key.pub` file and copy its contents.

2. In Snowflake, execute:

   ```sql
   ALTER USER your_username SET RSA_PUBLIC_KEY='paste_public_key_here';
   ```

   Replace `your_username` with your Snowflake username and `paste_public_key_here` with the content of your public key.

### 5. Set Environment Variables

To avoid hardcoding sensitive information, set the following environment variables:

```bash
export SNOWFLAKE_ACCOUNT='your_account_identifier'
export SNOWFLAKE_USER='your_username'
export SNOWFLAKE_PRIVATE_KEY_PATH='/path/to/rsa_key.p8'
```

On Windows, use:

```cmd
set SNOWFLAKE_ACCOUNT=your_account_identifier
set SNOWFLAKE_USER=your_username
set SNOWFLAKE_PRIVATE_KEY_PATH=C:\path\to\rsa_key.p8
```

### 6. Run Tests

Execute the test suite using pytest:

```bash
pytest -v
```

## Project Structure

```
snowflakeBD/
├── BusinessValidation/
│   └── test_business_logic.py
├── ConnectionTest/
│   └── test_connection.py
├── OrdersValidation/
│   └── test_orders.py
├── SupplierValidation/
│   └── test_suppliers.py
├── reports/
│   └── test_reports.py
├── conftest.py
└── requirements.txt
```

- **BusinessValidation/**: Contains tests for business logic validation.
- **ConnectionTest/**: Tests related to Snowflake connection.
- **OrdersValidation/**: Validations specific to orders data.
- **SupplierValidation/**: Validations specific to suppliers data.
- **reports/**: Scripts for generating test reports.
- **conftest.py**: Configuration file for pytest fixtures.
- **requirements.txt**: Lists Python dependencies.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For a visual guide on setting up key-pair authentication with Snowflake, you might find this video helpful:
<iframe width="560" height="315" src="https://www.youtube.com/embed/WdCLossuS8U?si=aG_wxXrAATaRFszY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
