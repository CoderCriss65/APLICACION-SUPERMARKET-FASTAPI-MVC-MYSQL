from locust import HttpUser, task, between

class SupermarketAPIUser(HttpUser):
    host = "http://localhost:8989"  # Especificar la URL base aquí
    wait_time = between(1, 3)
    
    # IDs de prueba (deben existir en tu base de datos)
    sucursal_id = 1
    departamento_id = 1
    empleado_id = 1
    cliente_id = 1
    categoria_id = 1
    proveedor_id = 1
    producto_id = 1
    venta_id = 1
    pedido_id = 1

    @task(3)
    def get_sucursales(self):
        self.client.get("/sucursales")


    @task(3)
    def get_departamentos(self):
        self.client.get("/departamentos")
    

    @task(3)
    def get_empleados(self):
        self.client.get("/empleados")
    

    @task(3)
    def get_clientes(self):
        self.client.get("/clientes")
    
    @task(2)
    def get_cliente_by_id(self):
        self.client.get(f"/clientes/{self.cliente_id}")
    
    @task(3)
    def get_categorias(self):
        self.client.get("/categorias")
    

    @task(3)
    def get_proveedores(self):
        self.client.get("/proveedores")
    

    @task(3)
    def get_productos(self):
        self.client.get("/productos")
    

    @task(3)
    def get_ventas(self):
        self.client.get("/ventas")

    @task(1)
    def get_root(self):
        self.client.get("/")
    
    @task(1)
    def health_check(self):
        self.client.get("/health")
