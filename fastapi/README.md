# FastAPI
> FastAPI is a python framework for building APIs.

Command for creating a project via uv (package manager like pip)
```bash
uv init project_name
```

Installing the fastapi 
```bash
uv add "fastapi[standard]"
# If you are using pip
pip install "fastapi[standard]"
```

A question might arise in your mind why would we put standard in installation of fastapi.
Because the standard package includes the following things - 

1. Fastapi
2. uvicorn - A HTTP Server.
3. Fastapi CLI 


For Running the fast api app, command:
```bash
uv run fastapi dev main.py
```