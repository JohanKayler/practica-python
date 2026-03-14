import sqlite3

# Crear y conectarse a una base de datos
conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

# Crear una tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio REAL,
        stock INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY,
        producto_id INTEGER,
        cantidad INTEGER,
        fecha TEXT
    )
""")

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (1, 'Laptop', 2500.00, 10)")
cursor.execute("INSERT INTO productos VALUES (2, 'Mouse', 45.00, 50)")
cursor.execute("INSERT INTO productos VALUES (3, 'Teclado', 120.00, 30)")
cursor.execute("INSERT INTO productos VALUES (4, 'Monitor', 850.00, 15)")
cursor.execute("INSERT INTO productos VALUES (5, 'Auriculares', 200.00, 25)")

cursor.execute("INSERT INTO ventas VALUES (1, 1, 2, '2024-01-15')")
cursor.execute("INSERT INTO ventas VALUES (2, 3, 5, '2024-01-16')")
cursor.execute("INSERT INTO ventas VALUES (3, 2, 1, '2024-01-17')")
cursor.execute("INSERT INTO ventas VALUES (4, 5, 3, '2024-01-18')")
cursor.execute("INSERT INTO ventas VALUES (5, 1, 1, '2024-01-19')")

conn.commit()  # guardar cambios
conn.close()   # cerrar conexión
print("Base de datos creada")