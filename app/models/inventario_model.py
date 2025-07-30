from app.config.database import get_db_connection

class InventarioModel:
    @staticmethod
    def get_inventario_sucursal(id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT i.*, p.nombre AS producto, p.precio 
            FROM inventario i
            JOIN productos p ON i.id_producto = p.id
            WHERE i.id_sucursal = %s
        """, (id_sucursal,))
        inventario = cursor.fetchall()
        cursor.close()
        conn.close()
        return inventario

    @staticmethod
    def get_by_producto_sucursal(id_producto, id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM inventario 
            WHERE id_producto = %s AND id_sucursal = %s
        """, (id_producto, id_sucursal))
        inventario = cursor.fetchone()
        cursor.close()
        conn.close()
        return inventario

    @staticmethod
    def update_stock(id_sucursal, id_producto, cantidad):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE inventario SET cantidad = %s "
            "WHERE id_sucursal = %s AND id_producto = %s",
            (cantidad, id_sucursal, id_producto)
        )
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows

    @staticmethod
    def create(id_producto, id_sucursal, cantidad, stock_minimo=10):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO inventario (id_producto, id_sucursal, cantidad, stock_minimo) "
            "VALUES (%s, %s, %s, %s)",
            (id_producto, id_sucursal, cantidad, stock_minimo)
        )
        conn.commit()
        inventario_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return inventario_id