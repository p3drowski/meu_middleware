from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API do Pedro funcionando!"}

@app.post("/calcular")
def calcular(payload: dict):
    numero = payload.get("numero")
    return {"resultado": numero * 10}
