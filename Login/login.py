from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import pymysql
from werkzeug.security import generate_password_hash

login_bp = Blueprint('login_bp', __name__,
                      template_folder='templates', 
                      static_folder='static',
                      static_url_path='/Login/static')

@login_bp.route('/login', methods=['POST', 'GET'])
def iniciar_sesion():
    return "Todo ok"
    
