from fastapi import APIRouter
from app.controllers.venta_controller import VentaController

router = APIRouter()

@router.post("/ventas")
async def create_venta(venta: dict):
    return VentaController.create_venta(venta)

@router.get("/sucursales/{id_sucursal}/ventas")
async def get_ventas_sucursal(id_sucursal: int):
    return VentaController.get_ventas_sucursal(id_sucursal)

@router.get("/ventas/{id_venta}/detalles")
async def get_detalles_venta(id_venta: int):
    return VentaController.get_detalles_venta(id_venta)


@router.get("/ventas")
async def get_all_ventas():
    return VentaController.get_all_ventas()