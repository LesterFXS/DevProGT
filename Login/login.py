from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'tu_secreto'  # Necesario para usar flash messages

# Datos de conexión a la base de datos MySQL
servidor = "bno7ox1wwkdqxekvdstn-mysql.services.clever-cloud.com"
usuario_bd = "u4ntvn9xowbmtzml"
contrasena_bd = "HWgirR2sFN6rmkKiOmaA"
base_datos = "bno7ox1wwkdqxekvdstn"

def crear_conexion():
    return pymysql.connect(
        host=servidor,
        user=usuario_bd,
        password=contrasena_bd,
        database=base_datos
    )

@app.route('/')
def index():
    return render_template('login.html')  # Asegúrate de que el nombre del archivo HTML sea correcto

@app.route('/submit', methods=['POST'])
def registrar_usuario():
    # Obtener los datos del formulario
    email = request.form['email']
    password = request.form['password']

    print(email)

    # Encriptar la contraseña
    hashed_password = generate_password_hash(password)

    # Conectar a la base de datos y registrar el usuario
    conexion = crear_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO login (correo, contra)
            VALUES (%s, %s)
            """,
            (email, hashed_password)
        )
        conexion.commit()
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('index'))  # Redirigir al formulario
    except Exception as e:
        flash(f"Error al registrar usuario: {e}", 'danger')
        return redirect(url_for('index'))  # Redirigir al formulario
    finally:
        cursor.close()
        conexion.close()

if __name__ == '__main__':  
    app.run(debug=True)