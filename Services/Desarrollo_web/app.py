from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Credenciales de la pasarela de pago
API_URL = "https://sandboxpayments.qpaypro.com/checkout/register_transaction_store"  # Reemplaza con el endpoint real
X_LOGIN = "visanetgt_qpay"
X_PRIVATE_KEY = "88888888888"
X_API_SECRET = "99999999999"

@app.route("/")
def home():
    return render_template("Desarrollo_Web.html")  # Carga el formulario HTML

@app.route("/pagar", methods=["POST"])
def procesar_pago():
    try:
        monto = request.form["monto"]  # Recibe los datos del formulario
        tarjeta_token = request.form["token"]

        # Datos para la pasarela de pago
        payload = {
            "x_login": X_LOGIN,
            "x_api_key": X_PRIVATE_KEY,
            "x_amount": "24.00",
            "x_currency_code": "GTQ",
            "x_first_name": "Usuario",
            "x_last_name": "Prueba",
            "x_phone": "24963214",
            "x_ship_to_address": "Ship address",
            "x_ship_to_city": "Ship City",
            "x_ship_to_country": "Guatemala",
            "x_ship_to_state": "0",
            "x_ship_to_zip": "1010",
            "x_ship_to_phone": "11223344",
            "x_description": "Order number: 123",
            "x_url_success": "",
            "x_url_error": "",
            "x_url_cancel": "URL_de_procedencia",
            "http_origin": "tuempresa.com",
            "x_company": "C/F",
            "x_address": "Address",
            "x_city": "City",
            "x_country": "Guatemala",
            "x_state": "0",
            "x_zip": "1201",
            "products":"[[\"Donativo - Cruz Roja Guatemalteca\",\"100\",\"\",\"1\",\"1\",\"1\"]]",
            "x_freight": "3.00",
            "taxes": "1.00",
            "x_email": "usuarioprueba@gmail.com",
            "x_type": "AUTH_ONLY",
            "x_method": "CC",
            "x_invoice_num": "123",
            "custom_fields": "{\"idSistema\": \"1009\",\"idCliente\": \"2025\",\"numerodeorden\":\"2585\"}",
            "x_visacuotas": "si",
            "x_relay_url": "RUTA_A_DONDE_DEBE_VOLVER_AL_FINALIZAR_PAGO",
            "origen": "PLUGIN",
            "store_type": "hostedpage",
            "x_discount": "0"
}
        # Enviar datos con POST a la pasarela de pago
        response = requests.post(API_URL, json=payload)
        respuesta_json = response.json()

        if response.status_code == 100 or 00:
            return f"<h3>Pago exitoso: {respuesta_json}</h3>"
        else:
            return f"<h3>Error en el pago: {respuesta_json}</h3>"

    except Exception as e:
        return f"<h3>Error interno: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(debug=True)





