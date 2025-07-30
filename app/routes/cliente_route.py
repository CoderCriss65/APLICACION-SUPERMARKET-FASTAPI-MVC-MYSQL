from fastapi import APIRouter
from app.controllers.cliente_controller import ClienteController

router = APIRouter()

@router.post("/clientes")
async def create_cliente(cliente: dict):
    return ClienteController.create(cliente)

@router.get("/clientes")
async def get_clientes():
    return ClienteController.get_all()

@router.get("/clientes/{id}")
async def get_cliente(id: int):
    return ClienteController.get_by_id(id)

@router.put("/clientes/{id}")
async def update_cliente(id: int, cliente: dict):
    return ClienteController.update(id, cliente)

@router.delete("/clientes/{id}")
async def delete_cliente(id: int):
    return ClienteController.delete(id)