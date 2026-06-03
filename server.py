from fastmcp import FastMCP
import sqlite3

from database import init_db, DB_NAME

# Inicializar base de datos
init_db()

# Crear servidor MCP
mcp = FastMCP("InventarioDB")


def get_connection():
    return sqlite3.connect(DB_NAME)


# ==========================
# Create Read Update Delete
# ==========================

@mcp.tool()
def crear_producto(nombre: str,
                   categoria: str,
                   cantidad: int,
                   precio: float):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO productos
        (nombre, categoria, cantidad, precio)
        VALUES (?, ?, ?, ?)
        """,
        (nombre, categoria, cantidad, precio)
    )

    conn.commit()
    conn.close()

    return "Producto creado correctamente"


@mcp.tool()
def consultar_producto(id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM productos WHERE id=?",
        (id,)
    )

    producto = cursor.fetchone()

    conn.close()

    if producto:
        return producto

    return "Producto no encontrado"


@mcp.tool()
def actualizar_producto(id: int, cantidad: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE productos
        SET cantidad=?
        WHERE id=?
        """,
        (cantidad, id)
    )

    conn.commit()
    conn.close()

    return "Producto actualizado"


@mcp.tool()
def eliminar_producto(id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM productos WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return "Producto eliminado"


@mcp.tool()
def listar_productos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM productos"
    )

    productos = cursor.fetchall()

    conn.close()

    return productos


# ==========================
# ANALÍTICA
# ==========================

@mcp.tool()
def calcular_valor_total_inventario():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(cantidad * precio)
        FROM productos
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


@mcp.tool()
def productos_agotados():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM productos
        WHERE cantidad = 0
        """
    )

    productos = cursor.fetchall()

    conn.close()

    return productos


@mcp.tool()
def producto_mas_costoso():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM productos
        ORDER BY precio DESC
        LIMIT 1
        """
    )

    producto = cursor.fetchone()

    conn.close()

    return producto


@mcp.tool()
def estadisticas_inventario():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            COUNT(*),
            AVG(cantidad),
            AVG(precio),
            SUM(cantidad * precio)
        FROM productos
        """
    )

    estadisticas = cursor.fetchone()

    conn.close()

    return estadisticas


if __name__ == "__main__":
    mcp.run()