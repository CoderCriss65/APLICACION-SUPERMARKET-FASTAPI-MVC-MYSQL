from fastapi import HTTPException
from app.models.producto_model import ProductoModel

class ProductoController:
    @staticmethod
    def create(producto_data: dict):
        return ProductoModel.create(
            producto_data['nombre'],
            producto_data['descripcion'],
            producto_data['precio'],
            producto_data['id_categoria'],
            producto_data['id_proveedor']
        )
    
    @staticmethod
    def get_all():
        return ProductoModel.get_all()
    
    @staticmethod
    def get_by_id(id: int):
        producto = ProductoModel.get_by_id(id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto
    
    @staticmethod
    def update(id: int, producto_data: dict):
        affected_rows = ProductoModel.update(
            id,
            producto_data['nombre'],
            producto_data['descripcion'],
            producto_data['precio'],
            producto_data['id_categoria'],
            producto_data['id_proveedor']
        )
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return {"message": "Producto actualizado"}
    
    @staticmethod
    def delete(id: int):
        affected_rows = ProductoModel.delete(id)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return {"message": "Producto eliminado"}