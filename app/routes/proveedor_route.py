from fastapi import APIRouter
from app.controllers.proveedor_controller import ProveedorController

router = APIRouter()

@router.post("/proveedores")
async def create_proveedor(proveedor: dict):
    return ProveedorController.create(proveedor)

@router.get("/proveedores")
async def get_proveedores():
    return ProveedorController.get_all()

@router.get("/proveedores/{id}")
async def get_proveedor(id: int):
    return ProveedorController.get_by_id(id)

@router.put("/proveedores/{id}")
async def update_proveedor(id: int, proveedor: dict):
    return ProveedorController.update(id, proveedor)

@router.delete("/proveedores/{id}")
async def delete_proveedor(id: int):
    return ProveedorController.delete(id)