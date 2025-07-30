from fastapi import HTTPException
from app.models.empleado_model import EmpleadoModel

class EmpleadoController:
    @staticmethod
    def create(empleado_data: dict):
        return EmpleadoModel.create(
            empleado_data['nombre'],
            empleado_data['apellido'],
            empleado_data['dni'],
            empleado_data['email'],
            empleado_data['password'],
            empleado_data['rol'],
            empleado_data['id_departamento']
        )
    
    @staticmethod
    def get_all():
        return EmpleadoModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        empleado = EmpleadoModel.get_by_id(id)
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return empleado
    
    @staticmethod
    def update(id: int, empleado_data: dict):
        affected_rows = EmpleadoModel.update(
            id,
            empleado_data['nombre'],
            empleado_data['apellido'],
            empleado_data['dni'],
            empleado_data['email'],
            empleado_data['rol'],
            empleado_data['id_departamento']
        )
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return {"message": "Empleado actualizado"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = EmpleadoModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return {"message": "Empleado eliminado"}