from app.config.database import get_db_connection

class ProductoModel:
    @staticmethod
    def create(nombre, descripcion, precio, id_categoria, id_proveedor):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, precio, id_categoria, id_proveedor) "
            "VALUES (%s, %s, %s, %s, %s)",
            (nombre, descripcion, precio, id_categoria, id_proveedor)
        )
        conn.commit()
        producto_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return producto_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, c.nombre AS categoria, pr.nombre AS proveedor 
            FROM productos p
            LEFT JOIN categorias c ON p.id_categoria = c.id
            LEFT JOIN proveedores pr ON p.id_proveedor = pr.id
        """)
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return productos

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, c.nombre AS categoria, pr.nombre AS proveedor 
            FROM productos p
            LEFT JOIN categorias c ON p.id_categoria = c.id
            LEFT JOIN proveedores pr ON p.id_proveedor = pr.id
            WHERE p.id = %s
        """, (id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        return producto

    @staticmethod
    def update(id, nombre, descripcion, precio, id_categoria, id_proveedor):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, "
            "id_categoria = %s, id_proveedor = %s WHERE id = %s",
            (nombre, descripcion, precio, id_categoria, id_proveedor, id)
        )
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows