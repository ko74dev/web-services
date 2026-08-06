from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Инициализируем шаблонизатор Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request, name: str = "Гость"):
    # Передаем параметры в шаблон
    return templates.TemplateResponse(request, "index.html", {"username": name})