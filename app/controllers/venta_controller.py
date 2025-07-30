from fastapi import HTTPException
from app.models.venta_model import VentaModel

class VentaController:
    
    @staticmethod
    def get_all_ventas():
        try:
            return VentaModel.get_all_ventas()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))




    @staticmethod
    def create_venta(venta_data: dict):
        try:
            return VentaModel.create_venta(
                venta_data['id_cliente'],
                venta_data['id_empleado'],
                venta_data['id_sucursal'],
                venta_data['total'],
                venta_data['detalles']
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @staticmethod
    def get_ventas_sucursal(id_sucursal: int):
        return VentaModel.get_ventas_by_sucursal(id_sucursal)
    
    @staticmethod
    def get_detalles_venta(id_venta: int):
        return VentaModel.get_detalles_venta(id_venta)

    
