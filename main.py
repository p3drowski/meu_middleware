from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Consulta Mockada", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DADOS MOCKADOS (já armazenados)
dados = {
    "clientes": [
        {
            "id": 1,
            "nome": "Pedro Pessoa",
            "cpf": "12345678900",
            "telefone": "31999999999",
            "email": "pedro@empresa.com"
        },
        {
            "id": 2,
            "nome": "João Silva",
            "cpf": "98765432100",
            "telefone": "31988888888",
            "email": "joao@empresa.com"
        }
    ],

    "boletos": [
        {
            "id": 101,
            "clienteId": 1,
            "vencimento": "2025-03-05",
            "valor": 129.90,
            "status": "aberto"
        },
        {
            "id": 102,
            "clienteId": 1,
            "vencimento": "2025-04-05",
            "valor": 129.90,
            "status": "pago"
        },
        {
            "id": 201,
            "clienteId": 2,
            "vencimento": "2025-03-10",
            "valor": 89.90,
            "status": "aberto"
        }
    ],

    "veiculos": [
        {
            "id": 1,
            "clienteId": 1,
            "placa": "HLB4F58",
            "modelo": "Uno Mille Fire",
            "chassi": "9BD123456AA6313614"
        }
    ]
}

@app.get("/")
def home():
    return {"status": "API Mockada Online"}

# CONSULTAR CLIENTE POR CPF
@app.get("/cliente/{cpf}")
def consultar_cliente(cpf: str):
    for c in dados["clientes"]:
        if c["cpf"] == cpf:
            return c
    return {"erro": "Cliente não encontrado"}

# CONSULTAR BOLETOS DO CLIENTE
@app.get("/boletos/{cpf}")
def boletos_cliente(cpf: str):
    cliente = next((c for c in dados["clientes"] if c["cpf"] == cpf), None)
    if not cliente:
        return {"erro": "Cliente não encontrado"}

    id_cliente = cliente["id"]
    boletos = [b for b in dados["boletos"] if b["clienteId"] == id_cliente]

    return {
        "cliente": cliente["nome"],
        "quantidade": len(boletos),
        "boletos": boletos
    }

# CONSULTAR VEÍCULOS DO CLIENTE
@app.get("/veiculos/{cpf}")
def veiculos_cliente(cpf: str):
    cliente = next((c for c in dados["clientes"] if c["cpf"] == cpf), None)
    if not cliente:
        return {"erro": "Cliente não encontrado"}

    id_cliente = cliente["id"]
    veiculos = [v for v in dados["veiculos"] if v["clienteId"] == id_cliente]

    return {
        "cliente": cliente["nome"],
        "veiculos": veiculos
    }
