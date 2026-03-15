import sqlite3

conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

# Todos los productos
cursor.execute("SELECT * FROM productos")
print(cursor.fetchall())

# Solo nombre y precio
cursor.execute("SELECT nombre, precio FROM productos")
print(cursor.fetchall())

# Productos con precio mayor a 100
cursor.execute("SELECT * FROM productos WHERE precio > 100")
print(cursor.fetchall())

# Ordenados por precio de mayor a menor
cursor.execute("SELECT * FROM productos ORDER BY precio DESC")
print(cursor.fetchall())

# Contar productos
cursor.execute("SELECT COUNT(*) FROM productos")
print(cursor.fetchone())

# Promedio de precios
cursor.execute("SELECT AVG(precio) FROM productos")
print(cursor.fetchone())

# Precio máximo y mínimo
cursor.execute("SELECT MAX(precio), MIN(precio) FROM productos")
print(cursor.fetchone())

# Productos con stock menor a 20, ordenados por stock
cursor.execute("SELECT nombre, stock FROM productos WHERE stock < 20 ORDER BY stock ASC")
print(cursor.fetchall())

# Escribe una consulta que muestre el nombre y precio 
# de los productos cuyo precio esté entre 100 y 1000 soles, ordenados por precio de menor a mayor. 
cursor.execute("SELECT nombre, precio FROM productos WHERE precio BETWEEN 100 AND 1000 ORDER BY precio ASC")
print(cursor.fetchall())


cursor.execute("""
    SELECT productos.nombre, productos.precio, ventas.cantidad, ventas.fecha
    FROM ventas
    JOIN productos ON ventas.producto_id = productos.id
""")
print(cursor.fetchall())

# Escribe una consulta que muestre el nombre del producto y 
# el total vendido (precio × cantidad) por cada venta, ordenado de mayor a menor total.
cursor.execute("""
               SElECT productos.nombre, productos.precio * ventas.cantidad AS total 
               FROM ventas 
               JOIN productos ON ventas.producto_id = productos.id
               ORDER BY total DESC
               """)
print(cursor.fetchall())


cursor.execute("""
    SELECT productos.nombre, SUM(ventas.cantidad) AS total_vendido
    FROM ventas
    JOIN productos ON ventas.producto_id = productos.id
    GROUP BY productos.nombre
""")
print(cursor.fetchall())

# ¿Cuánto dinero generó cada producto en total? 
# Muestra nombre y total de ingresos (precio × cantidad sumado), ordenado de mayor a menor.
cursor.execute("""SELECT productos.nombre, productos.precio * SUM(ventas.cantidad) AS total_ingresos 
               FROM ventas JOIN productos ON ventas.producto_id=productos.id 
               GROUP BY productos.nombre ORDER BY total_ingresos DESC
               """)
print(cursor.fetchall())

conn.close()
    
