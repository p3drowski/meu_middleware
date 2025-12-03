from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Host de Testes - Pedro",
    description="API simples publicada no Render",
    version="1.0.0"
)

# Liberação de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota GET
@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "Host funcionando corretamente no Render"
    }

# Rota POST para teste
@app.post("/processar")
def processar(payload: dict):
    nome = payload.get("nome", "Sem nome enviado")
    return {
        "mensagem_recebida": nome,
        "mensagem_retorno": f"Olá {nome}, seu host está respondendo!"
    }
