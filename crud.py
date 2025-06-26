import sqlite3

# Crear la base de datos y la tabla si no existen
def init_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# Crear un nuevo usuario
def crear_usuario(nombre, email):
    try:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        print("✅ Usuario creado exitosamente.")
    except sqlite3.IntegrityError:
        print("❌ Error: El email ya está registrado.")
    finally:
        conn.close()

# Leer todos los usuarios
def listar_usuarios():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    
    if usuarios:
        print("\n📋 Lista de usuarios:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Email: {usuario[2]}")
    else:
        print("\n⚠️ No hay usuarios registrados.")

# Actualizar un usuario
def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_email):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nuevo_nombre, nuevo_email, id_usuario))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("✅ Usuario actualizado.")
    else:
        print("❌ Usuario no encontrado.")
    
    conn.close()

# Eliminar un usuario
def eliminar_usuario(id_usuario):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("🗑️ Usuario eliminado.")
    else:
        print("❌ Usuario no encontrado.")
    
    conn.close()

# Menú para escoger diferentes opciones crud y salir del programa
def menu():
    while True:
        print("\n==== MENÚ CRUD USUARIO ====")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            crear_usuario(nombre, email)
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            id_usuario = input("ID del usuario a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_email = input("Nuevo email: ")
            actualizar_usuario(id_usuario, nuevo_nombre, nuevo_email)
        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            eliminar_usuario(id_usuario)
        elif opcion == "5":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    init_db()
    menu()

