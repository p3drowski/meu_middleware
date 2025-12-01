from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- CORS ---
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Rotas ---
@app.get("/")
def home():
    return {"mensagem": "API do Pedro funcionando!"}

@app.post("/calcular")
def calcular(payload: dict):
    numero = payload.get("numero")
    return {"resultado": numero * 10}
