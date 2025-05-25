import socket
import time
import json  # Importa el módulo json
from random import choice, randrange

HOST = "localhost"
PORT = 9999

# Datos de ejemplo en formato JSON
data = {
    "id": 1,
    "nombre": "chocolate",
    "cantidad": 25,
    "tipo": "",

}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conectado a {addr}")
        for i in range(1, 20):
            # Actualiza el JSON en cada iteración (ejemplo)
            data["id"] = i
            data["cantidad"] = 20 + (i % 10)
            data["tipo"] = choice(["v","r"])
            data["nombre"] = choice(["jabon","cafe","chocolate", "azucar"])
            # Convierte el diccionario a string JSON
            mensaje_json = json.dumps(data) + "\n"  # \n para separar mensajes

            # Envía el JSON
            conn.sendall(mensaje_json.encode())
            print(f"Enviado: {mensaje_json.strip()}")
            time.sleep(1)