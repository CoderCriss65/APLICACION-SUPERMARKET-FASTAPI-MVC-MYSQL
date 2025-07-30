from app.config.database import get_db_connection

class CategoriaModel:
    @staticmethod
    def create(nombre, descripcion):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO categorias (nombre, descripcion) VALUES (%s, %s)",
            (nombre, descripcion)
        )
        conn.commit()
        categoria_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return categoria_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        cursor.close()
        conn.close()
        return categorias

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias WHERE id = %s", (id,))
        categoria = cursor.fetchone()
        cursor.close()
        conn.close()
        return categoria

    @staticmethod
    def update(id, nombre, descripcion):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE categorias SET nombre = %s, descripcion = %s WHERE id = %s",
            (nombre, descripcion, id)
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
        cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows