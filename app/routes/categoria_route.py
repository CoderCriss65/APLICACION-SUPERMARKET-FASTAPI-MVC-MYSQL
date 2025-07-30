from fastapi import APIRouter
from app.controllers.categoria_controller import CategoriaController

router = APIRouter()

@router.post("/categorias")
async def create_categoria(categoria: dict):
    return CategoriaController.create(categoria)

@router.get("/categorias")
async def get_categorias():
    return CategoriaController.get_all()

@router.get("/categorias/{id}")
async def get_categoria(id: int):
    return CategoriaController.get_by_id(id)

@router.put("/categorias/{id}")
async def update_categoria(id: int, categoria: dict):
    return CategoriaController.update(id, categoria)

@router.delete("/categorias/{id}")
async def delete_categoria(id: int):
    return CategoriaController.delete(id)