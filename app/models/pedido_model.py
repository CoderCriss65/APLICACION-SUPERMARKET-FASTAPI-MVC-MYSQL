from app.config.database import get_db_connection

class PedidoModel:
    @staticmethod
    def create_pedido(id_proveedor, id_empleado, id_sucursal, total, detalles):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            conn.start_transaction()
            cursor.execute(
                "INSERT INTO pedidos (id_proveedor, id_empleado, id_sucursal, total, estado) "
                "VALUES (%s, %s, %s, %s, 'pendiente')",
                (id_proveedor, id_empleado, id_sucursal, total)
            )
            pedido_id = cursor.lastrowid

            for detalle in detalles:
                cursor.execute(
                    "INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario, subtotal) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (pedido_id, detalle['id_producto'], detalle['cantidad'], detalle['precio_unitario'], detalle['subtotal'])
                )

            conn.commit()
            return pedido_id
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def recibir_pedido(pedido_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            conn.start_transaction()
            cursor.execute(
                "UPDATE pedidos SET estado = 'recibido' WHERE id = %s",
                (pedido_id,)
            )

            cursor.execute("""
                SELECT dp.id_producto, dp.cantidad, p.id_sucursal 
                FROM detalles_pedido dp
                JOIN pedidos p ON dp.id_pedido = p.id
                WHERE dp.id_pedido = %s
            """, (pedido_id,))
            detalles = cursor.fetchall()

            for detalle in detalles:
                cursor.execute(
                    "UPDATE inventario SET cantidad = cantidad + %s "
                    "WHERE id_producto = %s AND id_sucursal = %s",
                    (detalle['cantidad'], detalle['id_producto'], detalle['id_sucursal'])
                )

            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_pedidos_sucursal(id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, pr.nombre AS proveedor, e.nombre AS empleado 
            FROM pedidos p
            JOIN proveedores pr ON p.id_proveedor = pr.id
            JOIN empleados e ON p.id_empleado = e.id
            WHERE p.id_sucursal = %s
        """, (id_sucursal,))
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pedidos