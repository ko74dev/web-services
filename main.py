from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user():
    return {"status": "success", "name": "Вайб-Кодер", "role": "Архитектор"}
