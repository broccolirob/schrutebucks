# Schrutebucks Blockchain

## Setup and Run Commands

### Activate the virtual environment

```shell
source schrutebucks/bin/activate
```

### Install all packages

```shell
pip install -r requirements.txt
```

### Run the tests

Make sure to activate the virtual environment first.

```shell
python -m pytest backend/tests
```

### Run the application and API

Make sure to activate the virtual environment first.

```shell
python -m backend.app
```

### Run a peer instance

```shell
export PEER=True && python -m backend.app
```
