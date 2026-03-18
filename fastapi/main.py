from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

data: list[dict] = [
    {
        "name": "Aditya",
        "age": 21,
        "city": "Mumbai"
    },
    {
        "name": "someone",
        "age": 22,
        "city": "Delhi"
    }
]

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/api/data")
def get_data():
    return data

# What If we want to return a HTML then for that
# We need to import the HTMLResponse from the fastapi.responses
# If we want to provide two routes with the same function we can do it in fastapi via this.
# If we want the api docs has to be show only the json apis not the html pages we can do it via a tag.
@app.get("/api/html", response_class=HTMLResponse, include_in_schema=False) # By means of the include_in_schema=False we can hide the api from the docs.
@app.get("/html", response_class=HTMLResponse, include_in_schema=False)
def get_html():
    return f"<h1>Hello, World!</h1>"

# NOTE: Fastapi automatically returns the output in JSON as of it is in list or dict.

# If you go to /docs - automatically generated swagger api documentation
# If you go to /redoc - This will gives the new documentation.
