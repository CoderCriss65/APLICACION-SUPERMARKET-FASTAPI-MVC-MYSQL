from fastapi import HTTPException
from app.models.departamento_model import DepartamentoModel

class DepartamentoController:
    @staticmethod
    def create(departamento_data: dict):
        return DepartamentoModel.create(
            departamento_data['nombre'],
            departamento_data['descripcion'],
            departamento_data['id_sucursal']
        )
    
    @staticmethod
    def get_all():
        return DepartamentoModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        departamento = DepartamentoModel.get_by_id(id)
        if not departamento:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return departamento
    
    @staticmethod
    def get_by_sucursal(id_sucursal: int):
        return DepartamentoModel.get_by_sucursal(id_sucursal)
    
    @staticmethod
    def update(id: int, departamento_data: dict):
        affected_rows = DepartamentoModel.update(
            id,
            departamento_data['nombre'],
            departamento_data['descripcion'],
            departamento_data['id_sucursal']
        )
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return {"message": "Departamento actualizado"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = DepartamentoModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return {"message": "Departamento eliminado"}