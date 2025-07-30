from app.config.database import get_db_connection

class ClienteModel:
    @staticmethod
    def create(nombre, apellido, email, telefono, direccion):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, apellido, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)",
            (nombre, apellido, email, telefono, direccion)
        )
        conn.commit()
        cliente_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return cliente_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return clientes

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
        cursor.close()
        conn.close()
        return cliente

    @staticmethod
    def update(id, nombre, apellido, email, telefono, direccion):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nombre = %s, apellido = %s, email = %s, telefono = %s, direccion = %s WHERE id = %s",
            (nombre, apellido, email, telefono, direccion, id)
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
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows