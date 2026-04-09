from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Backend online 🚀"}

@app.get("/teste")
def teste():
    return {"mensagem": "Funcionando!"}