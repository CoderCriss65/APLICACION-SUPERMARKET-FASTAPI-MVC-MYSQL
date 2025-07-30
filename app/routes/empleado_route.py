from fastapi import APIRouter
from app.controllers.empleado_controller import EmpleadoController

router = APIRouter()

@router.post("/empleados")
async def create_empleado(empleado: dict):
    return EmpleadoController.create(empleado)

@router.get("/empleados")
async def get_empleados():
    return EmpleadoController.get_all()

@router.get("/empleados/{id}")
async def get_empleado(id: int):
    return EmpleadoController.get_by_id(id)

@router.put("/empleados/{id}")
async def update_empleado(id: int, empleado: dict):
    return EmpleadoController.update(id, empleado)

@router.delete("/empleados/{id}")
async def delete_empleado(id: int):
    return EmpleadoController.delete(id)