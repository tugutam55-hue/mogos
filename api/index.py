import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes.scan import router as scan_router
from routes.config import router as config_router

app = FastAPI()

app.include_router(scan_router)
app.include_router(config_router)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "web", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "..", "web", "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=TEMPLATE_DIR)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )
