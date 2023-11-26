from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/index/", response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str] = Header(None)):
    films = [
        {'name': 'The Hunger Games', 'director': 'Gary Ross'},
        {'name': 'The Hunger Games: Catching Fire', 'director': 'Francis Lawrence'},
        {'name': 'The Hunger Games: Mockingjay – Part 1', 'director': 'Francis Lawrence'},
        {'name': 'The Hunger Games: Mockingjay – Part 2', 'director': 'Francis Lawrence'}
    ]
    contex = {'request': request, 'films': films}
    if hx_request:
        return templates.TemplateResponse('_table.html', contex)

    return templates.TemplateResponse('index.html', contex)