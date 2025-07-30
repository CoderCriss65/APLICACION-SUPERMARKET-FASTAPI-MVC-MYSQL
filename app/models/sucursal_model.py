from app.config.database import get_db_connection

class SucursalModel:
    @staticmethod
    def create(nombre, direccion, telefono):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sucursales (nombre, direccion, telefono) VALUES (%s, %s, %s)",
            (nombre, direccion, telefono)
        )
        conn.commit()
        sucursal_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return sucursal_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sucursales")
        sucursales = cursor.fetchall()
        cursor.close()
        conn.close()
        return sucursales

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sucursales WHERE id = %s", (id,))
        sucursal = cursor.fetchone()
        cursor.close()
        conn.close()
        return sucursal

    @staticmethod
    def update(id, nombre, direccion, telefono):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE sucursales SET nombre = %s, direccion = %s, telefono = %s WHERE id = %s",
            (nombre, direccion, telefono, id)
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
        cursor.execute("DELETE FROM sucursales WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows