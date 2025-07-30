from fastapi import FastAPI
from app.routes import (
    categoria_route,
    cliente_route,
    departamento_route,
    empleado_route,
    inventario_route,
    pedido_route,
    producto_route,
    proveedor_route,
    sucursal_route,
    venta_route
)

app = FastAPI(
    title="API de Supermercado",
    description="Sistema de gestión para minimarket con 4 sucursales",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Sucursales",
            "description": "Operaciones con sucursales"
        },
        {
            "name": "Departamentos",
            "description": "Gestión de departamentos por sucursal"
        },
        {
            "name": "Empleados",
            "description": "Gestión de empleados"
        },
        {
            "name": "Clientes",
            "description": "Gestión de clientes"
        },
        {
            "name": "Productos",
            "description": "Gestión de productos y categorías"
        },
        {
            "name": "Proveedores",
            "description": "Gestión de proveedores"
        },
        {
            "name": "Inventario",
            "description": "Gestión de inventario por sucursal"
        },
        {
            "name": "Ventas",
            "description": "Gestión de ventas y transacciones"
        },
        {
            "name": "Pedidos",
            "description": "Gestión de pedidos a proveedores"
        }
    ]
)

# Incluir todas las rutas
app.include_router(categoria_route.router, tags=["Productos"])
app.include_router(cliente_route.router, tags=["Clientes"])
app.include_router(departamento_route.router, tags=["Departamentos"])
app.include_router(empleado_route.router, tags=["Empleados"])
app.include_router(inventario_route.router, tags=["Inventario"])
app.include_router(pedido_route.router, tags=["Pedidos"])
app.include_router(producto_route.router, tags=["Productos"])
app.include_router(proveedor_route.router, tags=["Proveedores"])
app.include_router(sucursal_route.router, tags=["Sucursales"])
app.include_router(venta_route.router, tags=["Ventas"])

@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Bienvenido al API de Supermercado",
        "endpoints": {
            "sucursales": "/api/sucursales",
            "departamentos": "/api/departamentos",
            "empleados": "/api/empleados",
            "clientes": "/api/clientes",
            "productos": "/api/productos",
            "proveedores": "/api/proveedores",
            "categorias": "/api/categorias",
            "inventario": "/api/sucursales/{id}/inventario",
            "ventas": "/api/ventas",
            "pedidos": "/api/pedidos"
        }
    }

@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "ok", "message": "API en funcionamiento"}