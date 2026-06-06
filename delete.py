import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Borrar todos los registros
cursor.execute("DELETE FROM productos")

# Reiniciar el contador de IDs a 0
cursor.execute("DELETE FROM sqlite_sequence WHERE name='productos'")

conn.commit()
conn.close()
print("Registros eliminados e IDs reiniciados desde 1.")