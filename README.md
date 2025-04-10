# ZEBES: Zone for Emulated Behavior of External Services

## How to deploy ZEBES

### Local server

```uvicorn app.main:app --host 0.0.0.0 --port 8000```

### Docker server

```docker-compose up --build```

# Tips & Tricks

## Create virtual environment

```python -m venv venv```

```./venv/Scripts/activate.bat```

## Generate requirements file

```pip-compile .\requirements.in```

## Install requirements

```pip install -r requirements.txt```