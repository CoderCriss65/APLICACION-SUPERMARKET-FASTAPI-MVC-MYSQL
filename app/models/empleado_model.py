from app.config.database import get_db_connection

class EmpleadoModel:
    @staticmethod
    def create(nombre, apellido, dni, email, password, rol, id_departamento):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO empleados (nombre, apellido, dni, email, password, rol, id_departamento) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (nombre, apellido, dni, email, password, rol, id_departamento)
        )
        conn.commit()
        empleado_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return empleado_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.*, d.nombre AS departamento, s.nombre AS sucursal 
            FROM empleados e
            JOIN departamentos d ON e.id_departamento = d.id
            JOIN sucursales s ON d.id_sucursal = s.id
        """)
        empleados = cursor.fetchall()
        cursor.close()
        conn.close()
        return empleados

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.*, d.nombre AS departamento, s.nombre AS sucursal 
            FROM empleados e
            JOIN departamentos d ON e.id_departamento = d.id
            JOIN sucursales s ON d.id_sucursal = s.id
            WHERE e.id = %s
        """, (id,))
        empleado = cursor.fetchone()
        cursor.close()
        conn.close()
        return empleado

    @staticmethod
    def update(id, nombre, apellido, dni, email, rol, id_departamento):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE empleados SET nombre = %s, apellido = %s, dni = %s, email = %s, "
            "rol = %s, id_departamento = %s WHERE id = %s",
            (nombre, apellido, dni, email, rol, id_departamento, id)
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
        cursor.execute("DELETE FROM empleados WHERE id = %s", (id,))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows