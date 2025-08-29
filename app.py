from flask import Flask, render_template, jsonify, redirect, blueprints
from flask_mysqldb import MySQL
from Login.login import login_bp
from Sign_up.signup import signup_bp
from Index.index import index_bp
from Services.ControlServices.control_services import control_service_bp

app = Flask (__name__)

# Datos de conexión a la base de datos MySQL
app.config['MYSQL_HOST'] = 'bqg0wnfpwadbdjwz3uok-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'ufb8tcwkdrueue0j'
app.config['MYSQL_PASSWORD'] = 'jOGbe9EOgQHbh1KidwMP'
app.config['MYSQL_DB'] = 'bqg0wnfpwadbdjwz3uok'

conexion = MySQL(app)

login_bp.mysql = conexion
signup_bp.mysql = conexion

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(control_service_bp)

if __name__ == ('__main__'):
    app.run(debug=True)