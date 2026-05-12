from fastapi import FastAPI

app = FastAPI(title="DevOps TP API")

@app.get("/")
def root():
    return {"status": "ok", "message": "API funcionando"}

@app.get("/health")
def health():
    return {"healthy": True}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.post("/items")
def create_item(name: str):
    return {"created": True, "name": name}
