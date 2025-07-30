from fastapi import HTTPException
from app.models.categoria_model import CategoriaModel

class CategoriaController:
    @staticmethod
    def create(categoria_data: dict):
        return CategoriaModel.create(categoria_data['nombre'], categoria_data['descripcion'])
    
    @staticmethod
    def get_all():
        return CategoriaModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        categoria = CategoriaModel.get_by_id(id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria no encontrada")
        return categoria
    
    @staticmethod
    def update(id: int, categoria_data: dict):
        affected_rows = CategoriaModel.update(id, categoria_data['nombre'], categoria_data['descripcion'])
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Categoria no encontrada")
        return {"message": "Categoria actualizada"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = CategoriaModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Categoria no encontrada")
        return {"message": "Categoria eliminada"}