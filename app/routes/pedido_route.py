from fastapi import APIRouter
from app.controllers.pedido_controller import PedidoController

router = APIRouter()

@router.post("/pedidos")
async def create_pedido(pedido: dict):
    return PedidoController.create_pedido(pedido)

@router.put("/pedidos/{pedido_id}/recibir")
async def recibir_pedido(pedido_id: int):
    return PedidoController.recibir_pedido(pedido_id)

@router.get("/sucursales/{id_sucursal}/pedidos")
async def get_pedidos_sucursal(id_sucursal: int):
    return PedidoController.get_pedidos_sucursal(id_sucursal)