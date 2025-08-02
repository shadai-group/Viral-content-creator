from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from uuid import uuid4
from crear_guion import crear_guion_viral
import tempfile

# API Key ShadAI
os.environ["SHADAI_API_KEY"] = "API_KEY"

# Historial en memoria
historial = []

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "guion": None,
        "historial": historial
    })

@app.post("/", response_class=HTMLResponse)
async def generar(
    request: Request,
    tendenciaInput: str = Form(...),
    tipo: str = Form(...),
    imagen: UploadFile = File(None)
):
    imagen_path = None
    if imagen:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp_file.write(await imagen.read())
        temp_file.close()
        imagen_path = temp_file.name

    guion = await crear_guion_viral(tendenciaInput, tipo, imagen_path)

    historial.append({
        "id": str(uuid4()),
        "titulo": tendenciaInput.strip()[:30] + "...",
        "contenido": guion,
        "tipo": tipo
    })

    return templates.TemplateResponse("index.html", {
        "request": request,
        "guion": guion,
        "historial": historial
    })

@app.get("/guion/{guion_id}", response_class=HTMLResponse)
async def ver_guion(request: Request, guion_id: str):
    for g in historial:
        if g["id"] == guion_id:
            return templates.TemplateResponse("index.html", {
                "request": request,
                "guion": g["contenido"],
                "historial": historial
            })
    return templates.TemplateResponse("index.html", {
        "request": request,
        "guion": "⚠️ Guion no encontrado.",
        "historial": historial
    })

