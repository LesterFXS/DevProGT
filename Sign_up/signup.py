from flask import Flask, render_template, jsonify, Blueprint, request




signup_bp = Blueprint('signup_bp', __name__,
                      template_folder='templates',
                      static_folder='static',
                      static_url_path='/sign_up/static')


@signup_bp.route('/registrar', methods=['POST', "GET"])
def registrar_usuario():
    nombre = request.form.get('name')
    apellido = request.form.get('lastname')
    fecha = request.form.get('date')
    correo = request.form.get('email')
    contra = request.form.get('password')
    pais = request.form.get('country')

    mensaje = "Usuario registrado con éxito"

    try:
        cursor = signup_bp.mysql.connection.cursor()
        query = '''INSERT INTO usuarios (nombre_usuario, apellido_usuario, fecha_usuario, correo_usuario, contrasena_usuario, pais_usuario)
         VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (nombre, apellido, fecha, correo, contra, pais))
        signup_bp.mysql.connection.commit()
        cursor.close()
        
        return render_template('login.html', mensaje=mensaje)

    except Exception as ex:
        return f"Error al guardad datos: {ex}"