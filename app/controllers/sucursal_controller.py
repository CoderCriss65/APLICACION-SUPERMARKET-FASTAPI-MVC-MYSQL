from fastapi import HTTPException
from app.models.sucursal_model import SucursalModel

class SucursalController:
    @staticmethod
    def create(sucursal_data: dict):
        return SucursalModel.create(
            sucursal_data['nombre'],
            sucursal_data['direccion'],
            sucursal_data['telefono']
        )
    
    @staticmethod
    def get_all():
        return SucursalModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        sucursal = SucursalModel.get_by_id(id)
        if not sucursal:
            raise HTTPException(status_code=404, detail="Sucursal no encontrada")
        return sucursal
    
    @staticmethod
    def update(id: int, sucursal_data: dict):
        affected_rows = SucursalModel.update(
            id,
            sucursal_data['nombre'],
            sucursal_data['direccion'],
            sucursal_data['telefono']
        )
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Sucursal no encontrada")
        return {"message": "Sucursal actualizada"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = SucursalModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Sucursal no encontrada")
        return {"message": "Sucursal eliminada"}