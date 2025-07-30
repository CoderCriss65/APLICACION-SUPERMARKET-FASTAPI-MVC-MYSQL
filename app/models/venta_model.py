from app.config.database import get_db_connection

class VentaModel:
    @staticmethod
    def create_venta(id_cliente, id_empleado, id_sucursal, total, detalles):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            conn.start_transaction()
            cursor.execute(
                "INSERT INTO ventas (id_cliente, id_empleado, id_sucursal, total) "
                "VALUES (%s, %s, %s, %s)",
                (id_cliente, id_empleado, id_sucursal, total)
            )
            venta_id = cursor.lastrowid

            for detalle in detalles:
                cursor.execute(
                    "INSERT INTO detalles_venta (id_venta, id_producto, cantidad, precio_unitario, subtotal) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (venta_id, detalle['id_producto'], detalle['cantidad'], detalle['precio_unitario'], detalle['subtotal'])
                )

                cursor.execute(
                    "UPDATE inventario SET cantidad = cantidad - %s "
                    "WHERE id_producto = %s AND id_sucursal = %s",
                    (detalle['cantidad'], detalle['id_producto'], id_sucursal)
                )

            conn.commit()
            return venta_id
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_ventas_by_sucursal(id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.*, c.nombre AS cliente, e.nombre AS empleado
            FROM ventas v
            LEFT JOIN clientes c ON v.id_cliente = c.id
            JOIN empleados e ON v.id_empleado = e.id
            WHERE v.id_sucursal = %s
        """, (id_sucursal,))
        ventas = cursor.fetchall()
        cursor.close()
        conn.close()
        return ventas

    @staticmethod
    def get_detalles_venta(id_venta):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT dv.*, p.nombre AS producto 
            FROM detalles_venta dv
            JOIN productos p ON dv.id_producto = p.id
            WHERE dv.id_venta = %s
        """, (id_venta,))
        detalles = cursor.fetchall()
        cursor.close()
        conn.close()
        return detalles


    @staticmethod
    def get_all_ventas():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.*, c.nombre AS cliente, e.nombre AS empleado, s.nombre AS sucursal
            FROM ventas v
            LEFT JOIN clientes c ON v.id_cliente = c.id
            JOIN empleados e ON v.id_empleado = e.id
            JOIN sucursales s ON v.id_sucursal = s.id
        """)
        ventas = cursor.fetchall()
        cursor.close()
        conn.close()
        return ventas