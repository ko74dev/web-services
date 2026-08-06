from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

# Настройка шаблонов
templates_dir = Path(__file__).parent / "templates"
env = Environment(
    loader=FileSystemLoader(str(templates_dir)),
    autoescape=True,
    auto_reload=True
)

# Пример списка задач
tasks_db = [
    {"id": 1, "title": "Создать проект FastAPI", "description": "Инициализировать проект", "completed": True},
    {"id": 2, "title": "Добавить шаблоны Jinja2", "description": "Настроить рендеринг HTML", "completed": True},
    {"id": 3, "title": "Создать страницу задач", "description": "Отобразить список задач", "completed": False}
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    template = env.get_template("index.html")
    html = template.render(request=request, tasks=tasks_db)
    return HTMLResponse(content=html)

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
