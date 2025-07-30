from app.config.database import get_db_connection

class ProveedorModel:
    @staticmethod
    def create(nombre, contacto, telefono, direccion, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO proveedores (nombre, contacto, telefono, direccion, email) "
            "VALUES (%s, %s, %s, %s, %s)",
            (nombre, contacto, telefono, direccion, email)
        )
        conn.commit()
        proveedor_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return proveedor_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        cursor.close()
        conn.close()
        return proveedores

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id,))
        proveedor = cursor.fetchone()
        cursor.close()
        conn.close()
        return proveedor

    @staticmethod
    def update(id, nombre, contacto, telefono, direccion, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE proveedores SET nombre = %s, contacto = %s, telefono = %s, "
            "direccion = %s, email = %s WHERE id = %s",
            (nombre, contacto, telefono, direccion, email, id)
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
        cursor.execute("DELETE FROM proveedores WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows