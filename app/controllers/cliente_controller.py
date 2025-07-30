from fastapi import HTTPException
from app.models.cliente_model import ClienteModel

class ClienteController:
    @staticmethod
    def create(cliente_data: dict):
        return ClienteModel.create(
            cliente_data['nombre'],
            cliente_data['apellido'],
            cliente_data['email'],
            cliente_data['telefono'],
            cliente_data['direccion']
        )
    
    @staticmethod
    def get_all():
        return ClienteModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        cliente = ClienteModel.get_by_id(id)
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        return cliente
    
    @staticmethod
    def update(id: int, cliente_data: dict):
        affected_rows = ClienteModel.update(
            id,
            cliente_data['nombre'],
            cliente_data['apellido'],
            cliente_data['email'],
            cliente_data['telefono'],
            cliente_data['direccion']
        )
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        return {"message": "Cliente actualizado"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = ClienteModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        return {"message": "Cliente eliminado"}