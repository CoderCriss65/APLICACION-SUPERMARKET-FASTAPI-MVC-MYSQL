from fastapi import HTTPException
from app.models.proveedor_model import ProveedorModel

class ProveedorController:
    @staticmethod
    def create(proveedor_data: dict):
        return ProveedorModel.create(
            proveedor_data['nombre'],
            proveedor_data['contacto'],
            proveedor_data['telefono'],
            proveedor_data['direccion'],
            proveedor_data['email']
        )
    
    @staticmethod
    def get_all():
        return ProveedorModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        proveedor = ProveedorModel.get_by_id(id)
        if not proveedor:
            raise HTTPException(status_code=404, detail="Proveedor no encontrado")
        return proveedor
    
    @staticmethod
    def update(id: int, proveedor_data: dict):
        affected_rows = ProveedorModel.update(
            id,
            proveedor_data['nombre'],
            proveedor_data['contacto'],
            proveedor_data['telefono'],
            proveedor_data['direccion'],
            proveedor_data['email']
        )
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Proveedor no encontrado")
        return {"message": "Proveedor actualizado"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = ProveedorModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Proveedor no encontrado")
        return {"message": "Proveedor eliminado"}