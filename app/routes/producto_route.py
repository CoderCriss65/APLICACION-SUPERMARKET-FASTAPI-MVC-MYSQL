from fastapi import APIRouter
from app.controllers.producto_controller import ProductoController

router = APIRouter()

@router.post("/productos")
async def create_producto(producto: dict):
    return ProductoController.create(producto)

@router.get("/productos")
async def get_productos():
    return ProductoController.get_all()

@router.get("/productos/{id}")
async def get_producto(id: int):
    return ProductoController.get_by_id(id)

@router.put("/productos/{id}")
async def update_producto(id: int, producto: dict):
    return ProductoController.update(id, producto)

@router.delete("/productos/{id}")
async def delete_producto(id: int):
    return ProductoController.delete(id)