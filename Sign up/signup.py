from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'tu_secreto'  # Necesario para usar flash messages

# Datos de conexión a la base de datos MySQL
servidor = "bb3itdt4uanlibigzvu2-mysql.services.clever-cloud.com"
usuario_bd = "uhaydkjlu1lcktzd"
contrasena_bd = "Ff9mV6czXXbWY812vSmo"
base_datos = "bb3itdt4uanlibigzvu2"

def crear_conexion():
    return pymysql.connect(
        host=servidor,
        user=usuario_bd,
        password=contrasena_bd,
        database=base_datos
    )

@app.route('/')
def index():
    return render_template('signup.html')  # Asegúrate de que el nombre del archivo HTML sea correcto

@app.route('/submit', methods=['POST'])
def registrar_usuario():
    # Obtener los datos del formulario
    name = request.form['name']
    lastname = request.form['lastname']
    date = request.form['date']
    email = request.form['email']
    password = request.form['password']

    print(name, lastname, date, email)

    # Encriptar la contraseña
    hashed_password = generate_password_hash(password)

    # Conectar a la base de datos y registrar el usuario
    conexion = crear_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO signup (nombre, apellido, fecha_nacimiento, correo, contrasena)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (name, lastname, date, email, hashed_password)
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