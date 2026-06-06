"""
Script de pruebas para el servidor MCP de Inventario.
Ejecutar con: python test_server.py
"""
import sqlite3
import sys
import os

# Agregar directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_db, DB_NAME

# ── Inicializar base de datos ──────────────────────────
init_db()

def get_connection():
    return sqlite3.connect(DB_NAME)

# ── Funciones duplicadas para prueba directa ───────────
def crear_producto(nombre, categoria, cantidad, precio):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
        (nombre, categoria, cantidad, precio)
    )
    conn.commit()
    pid = cursor.lastrowid
    conn.close()
    return f"Producto '{nombre}' creado con ID {pid}."

def consultar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1], "categoria": row[2], "cantidad": row[3], "precio": row[4]}
    return {"error": f"Producto con ID {id} no encontrado."}

def actualizar_producto(id, cantidad):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
    conn.commit()
    conn.close()
    return f"Producto ID {id} actualizado. Nueva cantidad: {cantidad}."

def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return f"Producto ID {id} eliminado."

def listar_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nombre": r[1], "categoria": r[2], "cantidad": r[3], "precio": r[4]} for r in rows]

def calcular_valor_total_inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(cantidad * precio) FROM productos")
    total = cursor.fetchone()[0]
    conn.close()
    return {"valor_total_inventario": round(total, 2) if total else 0}

def productos_agotados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad = 0")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nombre": r[1], "categoria": r[2], "cantidad": r[3], "precio": r[4]} for r in rows]

def producto_mas_costoso():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY precio DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1], "categoria": row[2], "cantidad": row[3], "precio": row[4]}
    return {"error": "No hay productos."}

def estadisticas_inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), AVG(cantidad), AVG(precio), SUM(cantidad * precio) FROM productos")
    total, prom_cant, prom_precio, valor = cursor.fetchone()
    conn.close()
    return {
        "total_productos": total or 0,
        "promedio_cantidad": round(prom_cant, 2) if prom_cant else 0,
        "promedio_precio": round(prom_precio, 2) if prom_precio else 0,
        "valor_total": round(valor, 2) if valor else 0
    }

# ══════════════════════════════════════════════════════
# PRUEBAS
# ══════════════════════════════════════════════════════

print("=" * 60)
print("   PRUEBAS DEL SERVIDOR MCP - INVENTARIO")
print("   Computación Cognitiva para Big Data")
print("=" * 60)

# ── Prueba 1: Crear 5 productos ────────────────────────
print("\n PRUEBA 1: Crear 5 productos")
print("-" * 40)
print(crear_producto("Laptop Dell Inspiron", "Electrónica", 15, 2500000.0))
print(crear_producto("Mouse Inalámbrico Logitech", "Periféricos", 30, 85000.0))
print(crear_producto("Teclado Mecánico HyperX", "Periféricos", 0, 320000.0))
print(crear_producto("Monitor LG 27 pulgadas", "Electrónica", 8, 1200000.0))
print(crear_producto("Disco Duro SSD 1TB", "Almacenamiento", 20, 450000.0))

# --- Listar todos los productos ──────────────
print("\n Listar todos los productos")
print("-" * 40)
productos = listar_productos()
print(f"  Total productos en inventario: {len(productos)}")
for p in productos:
    print(f"  [{p['id']}] {p['nombre']} | Cat: {p['categoria']} | Cant: {p['cantidad']} | Precio: ${p['precio']:,.0f}")

# ── Prueba 2: Consultar producto por ID ───────────────
print("\n PRUEBA 2: Consultar producto con ID 1")
print("-" * 40)
result = consultar_producto(1)
for k, v in result.items():
    print(f"  {k}: {v}")

# ── Prueba 3: Actualizar cantidad ─────────────────────
print("\n PRUEBA 3: Actualizar cantidad del producto ID 2")
print("-" * 40)
print(actualizar_producto(2, 50))
result = consultar_producto(2)
print(f"  Nueva cantidad verificada: {result['cantidad']}")

# ── Prueba 4: Eliminar producto ───────────────────────
print("\n  PRUEBA 4: Eliminar producto ID 5")
print("-" * 40)
print(eliminar_producto(5))

# ── Prueba 5: Listar todos los productos ──────────────
print("\n PRUEBA 5: Listar todos los productos")
print("-" * 40)
productos = listar_productos()
print(f"  Total productos en inventario: {len(productos)}")
for p in productos:
    print(f"  [{p['id']}] {p['nombre']} | Cat: {p['categoria']} | Cant: {p['cantidad']} | Precio: ${p['precio']:,.0f}")

# ── Prueba 6: Valor total del inventario ──────────────
print("\n PRUEBA 6: Calcular valor total del inventario")
print("-" * 40)
result = calcular_valor_total_inventario()
print(f"  Valor total: ${result['valor_total_inventario']:,.2f}")

# ── Prueba 7: Productos agotados ──────────────────────
print("\n PRUEBA 7: Consultar productos agotados (cantidad = 0)")
print("-" * 40)
agotados = productos_agotados()
if agotados:
    for p in agotados:
        print(f" [{p['id']}] {p['nombre']} - AGOTADO")
else:
    print("  No hay productos agotados actualmente.")

# ── Prueba 8: Producto más costoso ────────────────────
print("\n PRUEBA 8: Identificar el producto más costoso")
print("-" * 40)
mas_caro = producto_mas_costoso()
print(f"  Producto más costoso: {mas_caro['nombre']}")
print(f"  Precio: ${mas_caro['precio']:,.2f}")
print(f"  Categoría: {mas_caro['categoria']}")

# ── Prueba 9: Estadísticas generales ─────────────────
print("\n PRUEBA 9: Estadísticas generales del inventario")
print("-" * 40)
stats = estadisticas_inventario()
print(f"  Total productos:      {stats['total_productos']}")
print(f"  Cantidad promedio:    {stats['promedio_cantidad']}")
print(f"  Precio promedio:      ${stats['promedio_precio']:,.2f}")
print(f"  Valor total:          ${stats['valor_total']:,.2f}")

print("\n" + "=" * 60)
print("TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
print("=" * 60)
