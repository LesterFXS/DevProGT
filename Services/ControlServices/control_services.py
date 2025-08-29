from flask import Flask, Blueprint, render_template, jsonify, request
from flask_mysqldb import MySQL

control_service_bp = Blueprint('control_service_bp', __name__,
                               template_folder='templates', 
                               static_folder='stacit',
                               static_url_path="/Services/ControlServices/static")

#Registrar los datos
@control_service_bp.route('/registrar_datos', methods=['POST', 'GET'])
def registrar_datos():
    
    nombre = request.form.get('cliente_rec')
    telefono =request.form.get('telefono_rec')
    email = request.form.get('email_rec')
    equipo = request.form.get('equipo_rec')
    marca = request.form.get('marca_rec')
    modelo = request.form.get('modelo_rec')
    serie =  request.form.get('serie_rec')
    fecha = request.form.get('fecha_rec')
    hora = request.form.get('hora_rec')
    falla = request.form.get('falla_rec')
    accesorios = request.form.get('accesorios_rec')
    prioridad = request.form.get('prioridad_rec')
    garantia = request.form.get('garantia_rec')
    observaciones = request.form.get('observaciones_rec')

    try: 
        cursor = control_service_bp.mysql.connection.cursor()
        query = '''INSERT INTO cs_recepcion (
                recepcion_nombre_cliente,
                recepcion_telefono_cliente,
                recepcion_email_cliente,
                recepcion_tipo_equipo,
                recepcion_marca_equipo,
                recepcion_modelo_equipo,
                recepcion_noSerie_equipo,
                recepcion_fecha_recepcioin,
                recepcion_hora_recepcion,
                recepcion_descripcion_falla,
                recepcion_accesorios_equipo,
                recepcion_prioridad,
                recepcion_equipo_garantía,
                recepcion_observaciones
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'''
        cursor.execute(query, (nombre, telefono, email, equipo, marca , modelo, serie, fecha, hora, falla, accesorios, prioridad, garantia, observaciones ))
        control_service_bp.mysql.connection.commit()
        cursor.close()


    except Exception as ex:
        return jsonify(f"Error en el registor: {ex}")