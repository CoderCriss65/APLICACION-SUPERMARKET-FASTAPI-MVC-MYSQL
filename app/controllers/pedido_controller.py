from fastapi import HTTPException
from app.models.pedido_model import PedidoModel

class PedidoController:
    @staticmethod
    def create_pedido(pedido_data: dict):
        return PedidoModel.create_pedido(
            pedido_data['id_proveedor'],
            pedido_data['id_empleado'],
            pedido_data['id_sucursal'],
            pedido_data['total'],
            pedido_data['detalles']
        )
    
    @staticmethod
    def recibir_pedido(pedido_id: int):
        try:
            PedidoModel.recibir_pedido(pedido_id)
            return {"message": "Pedido recibido y stock actualizado"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @staticmethod
    def get_pedidos_sucursal(id_sucursal: int):
        return PedidoModel.get_pedidos_sucursal(id_sucursal)