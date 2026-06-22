from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def get_info():
    return {
        "status": "running",
        "contact": {
            "name": "Gopinath",
            "contact.no": 11111
        },
        "skills": ["python", "java", "sql"]
    }