from flask import Flask, Blueprint, render_template, jsonify, request
from flask_mysqldb import MySQL

control_service_bp = Blueprint('control_service_bp', __name__,
                               template_folder='templates', 
                               static_folder='stacit',
                               static_url_path="/Services/ControlServices/static")

