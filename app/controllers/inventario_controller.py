from fastapi import HTTPException
from app.models.inventario_model import InventarioModel

class InventarioController:
    @staticmethod
    def get_inventario_sucursal(id_sucursal: int):
        return InventarioModel.get_inventario_sucursal(id_sucursal)
    
    @staticmethod
    def update_stock(id_sucursal: int, id_producto: int, cantidad: int):
        affected_rows = InventarioModel.update_stock(id_sucursal, id_producto, cantidad)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
        return {"message": "Stock actualizado"}
    
    @staticmethod
    def create(inventario_data: dict):
        return InventarioModel.create(
            inventario_data['id_producto'],
            inventario_data['id_sucursal'],
            inventario_data['cantidad'],
            inventario_data.get('stock_minimo', 10)
        )