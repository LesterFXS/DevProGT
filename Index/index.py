from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import pymysql
from werkzeug.security import generate_password_hash

index_bp = Blueprint('index_bp', __name__,
                      template_folder='templates', 
                      static_folder='static',
                      static_url_path='/Index/static')

@index_bp.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@index_bp.route('/login', methods=['POST', 'GET'])
def go_login():
    return render_template('login.html')

@index_bp.route('/signup', methods=['POST', 'GET'])
def go_signup():
    return render_template('signup.html')

#Modulos
@index_bp.route('/Control_de_servicios', methods=['POST', 'GET'])
def go_control_services():
    return render_template ('control_services.html')

@index_bp.route('/control_de_servicios_consultar', methods=['POST', 'GET'])
def go_control_services_consultar():
    return render_template('cs_consultar.html')

@index_bp.route('/control_de_servicios_recepcion', methods=['POST', 'GET'])
def go_control_services_recepcion():
    return render_template('cs_recepcion.html')

@index_bp.route('/control_de_servicios_actualizar', methods=['POST', 'GET'])
def go_control_services_actualizar():
    return render_template('cs_actualizar.html')