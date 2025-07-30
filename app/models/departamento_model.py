from app.config.database import get_db_connection

class DepartamentoModel:
    @staticmethod
    def create(nombre, descripcion, id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO departamentos (nombre, descripcion, id_sucursal) VALUES (%s, %s, %s)",
            (nombre, descripcion, id_sucursal)
        )
        conn.commit()
        departamento_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return departamento_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departamentos")
        departamentos = cursor.fetchall()
        cursor.close()
        conn.close()
        return departamentos

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departamentos WHERE id = %s", (id,))
        departamento = cursor.fetchone()
        cursor.close()
        conn.close()
        return departamento

    @staticmethod
    def get_by_sucursal(id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departamentos WHERE id_sucursal = %s", (id_sucursal,))
        departamentos = cursor.fetchall()
        cursor.close()
        conn.close()
        return departamentos

    @staticmethod
    def update(id, nombre, descripcion, id_sucursal):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE departamentos SET nombre = %s, descripcion = %s, id_sucursal = %s WHERE id = %s",
            (nombre, descripcion, id_sucursal, id)
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
        cursor.execute("DELETE FROM departamentos WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows