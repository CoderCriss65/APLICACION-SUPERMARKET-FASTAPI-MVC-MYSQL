from fastapi import APIRouter
from app.controllers.sucursal_controller import SucursalController

router = APIRouter()

@router.post("/sucursales")
async def create_sucursal(sucursal: dict):
    return SucursalController.create(sucursal)

@router.get("/sucursales")
async def get_sucursales():
    return SucursalController.get_all()

@router.get("/sucursales/{id}")
async def get_sucursal(id: int):
    return SucursalController.get_by_id(id)

@router.put("/sucursales/{id}")
async def update_sucursal(id: int, sucursal: dict):
    return SucursalController.update(id, sucursal)

@router.delete("/sucursales/{id}")
async def delete_sucursal(id: int):
    return SucursalController.delete(id)