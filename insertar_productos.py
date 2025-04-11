import sqlite3

conexion = sqlite3.connect("pos.db")
cursor = conexion.cursor()

# Una vez agregados los productos, se pueden borrar de este código y si en un futuro es necesario agregar más, solo se agrega el nuevo producto

productos = [
    ("035698745632", "Laptop HP", 15000.00, 5),
    ("258963147852", "Mouse Logitech", 500.00, 20),
    ("789654123023", "Teclado mecánico", 1200.00, 15),
    ("785452214587", "Monitor Samsung 24", 4000.00, 10),
    ("349827105623", "Auriculares Gamer", 2500.00, 8),
    ("708432195674", "Smartphone Samsung", 12000.00, 6),
    ("120984376581", "Impresora HP", 3000.00, 7),
    ("563729841025", "Tablet Lenovo", 7500.00, 5),
    ("892347615092", "Disco Duro 1TB", 2000.00, 12),
    ("437910284653", "Memoria USB 64GB", 300.00, 25),
    ("901284763159", "Camiseta Nike", 600.00, 30),
    ("274819365047", "Pantalón Levis", 1200.00, 20),
    ("685219347601", "Zapatillas Adidas", 1800.00, 15),
    ("312890475628", "Sudadera Puma", 1500.00, 18),
    ("785032149608", "Reloj Casio", 800.00, 10),
    ("613429875120", "Gorra New Era", 500.00, 25),
    ("940281736549", "Mochila Jansport", 1300.00, 10),
    ("308176245901", "Lentes de sol Ray-Ban", 2500.00, 7),
    ("726304891752", "Cinturón de cuero", 700.00, 12),
    ("154928370614", "Chaqueta de cuero", 3500.00, 5),
    ("879613204578", "Monitor Vertical Samsung 32", 11500.00, 50)
]

for plu, nombre, precio, stock in productos:
    cursor.execute("SELECT COUNT(*) FROM productos WHERE plu = ?", (plu,))
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO productos (plu, nombre, precio, stock) VALUES (?, ?, ?, ?)",
                      (plu, nombre, precio, stock))
    else:
        print(f"Producto con PLU {plu} ya existe, omitiendo.")

conexion.commit()
conexion.close()
print("Productos agregados correctamente.")
