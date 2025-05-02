# Talk to Me

A FastAPI web service with Swagger UI support.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies and the package:
```bash
pip install -r requirements.txt
pip install -e .  # Install the package in development mode
```

## Configuration

The service uses a configuration file (`conf.ini`) to manage settings. The configuration file includes:

- Server settings (host, port, reload)
- Application settings (title, description, version)
- CORS settings

Example configuration:
```ini
[server]
host = 0.0.0.0
port = 8000
reload = true

[app]
title = Talk to Me API
description = A FastAPI web service with Swagger UI support
version = 0.1.0

[cors]
allow_origins = ["*"]
allow_credentials = true
allow_methods = ["*"]
allow_headers = ["*"]
```

## Running the Service

After installation, you can run the service using the command-line tool:
```bash
talk-to-me -c conf.ini
```

Alternatively, you can run it using the Python module:
```bash
python -m talk_to_me.cli -c conf.ini
```

The service will be available at:
- Main API: http://localhost:8000 (or http://your-ip:8000 from other machines)
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Note: Running on `0.0.0.0` makes the service accessible from other machines on the network. For local development only, you can modify the `host` setting in `conf.ini` to `127.0.0.1`.

## API Endpoints

- `GET /`: Hello endpoint
- `GET /health`: Health check endpoint

## Development

The project structure is as follows:
```
talk-to-me/
├── talk_to_me/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── cli.py
├── conf.ini
├── requirements.txt
├── setup.py
└── README.md
```
