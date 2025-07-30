from fastapi import APIRouter
from app.controllers.inventario_controller import InventarioController

router = APIRouter()

@router.get("/sucursales/{id_sucursal}/inventario")
async def get_inventario_sucursal(id_sucursal: int):
    return InventarioController.get_inventario_sucursal(id_sucursal)

@router.put("/inventario/{id_sucursal}/{id_producto}")
async def update_stock(id_sucursal: int, id_producto: int, cantidad: int):
    return InventarioController.update_stock(id_sucursal, id_producto, cantidad)

@router.post("/inventario")
async def create_inventario(inventario: dict):
    return InventarioController.create(inventario)