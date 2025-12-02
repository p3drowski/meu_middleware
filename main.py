from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(
    title="Middleware Mockado do Pedro",
    description="API local simulando um host para usar no Studio",
    version="1.0.0"
)

# CORS liberado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Função para carregar mocks
def load_mock(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

# ---------- ROTA PRINCIPAL ----------
@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "Middleware mockado funcionando!",
        "autor": "Pedro Pessoa"
    }

# ---------- ROTA CLIENTE ----------
@app.post("/cliente/dados")
def cliente_dados(payload: dict):
    dados = load_mock("mock/cliente.json")

    # Exemplo de transformação
    dados["nomeCompleto"] = dados["nome"].upper()

    return dados

# ---------- ROTA VEICULOS ----------
@app.post("/infornet/veiculos")
def listar_veiculos(payload: dict):
    veiculos = load_mock("mock/veiculos.json")
    return {"qtdVeiculos": len(veiculos), "veiculos": veiculos}

# ---------- ROTA BOLETOS ----------
@app.post("/boletos")
def boletos(payload: dict):
    boletos = load_mock("mock/boletos.json")

    # Simular transformação igual middleware real
    boletos_transformados = [
        {
            "codigo": b["codigo"],
            "descricao": b["descricao"],
            "valorFormatado": f"R${b['valor']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "vencimento": b["vencimento"],
            "situacao": "PENDENTE"
        }
        for b in boletos
    ]

    return {"boletos": boletos_transformados}
