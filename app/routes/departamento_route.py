from fastapi import APIRouter
from app.controllers.departamento_controller import DepartamentoController

router = APIRouter()

@router.post("/departamentos")
async def create_departamento(departamento: dict):
    return DepartamentoController.create(departamento)

@router.get("/departamentos")
async def get_departamentos():
    return DepartamentoController.get_all()

@router.get("/departamentos/{id}")
async def get_departamento(id: int):
    return DepartamentoController.get_by_id(id)

@router.get("/sucursales/{id_sucursal}/departamentos")
async def get_departamentos_sucursal(id_sucursal: int):
    return DepartamentoController.get_by_sucursal(id_sucursal)

@router.put("/departamentos/{id}")
async def update_departamento(id: int, departamento: dict):
    return DepartamentoController.update(id, departamento)

@router.delete("/departamentos/{id}")
async def delete_departamento(id: int):
    return DepartamentoController.delete(id)