import zoneinfo
import time

from datetime import datetime
from fastapi import FastAPI, HTTPException, Request, Depends, status, APIRouter, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import Customer, Transaction, Invoice
from db import SessionDep, create_all_tables
from sqlmodel import select
from src.routers import customers, transactions, plans
from typing import Annotated
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(lifespan=create_all_tables)
templates = Jinja2Templates(directory="../templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

router = APIRouter()
security = HTTPBasic()

"""@app.get("/")
def test(request:Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={"request": request}
    )"""

@router.get("/login", tags=["login"])
def mostrar_login(request: Request):
    #return templates.TemplateResponse("index.html", {"request": request})
    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}
    )


@router.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print(credentials)
    if credentials.username == "leonardo" and credentials.password == "123456789":
        return {"message": f"hola, {credentials.username}!"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no existe")