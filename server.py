from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/api/comentarios', methods=['GET'])
def get_comentarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM comentarios ORDER BY hora DESC")
    comentarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(comentarios)

@app.route('/api/comentarios', methods=['POST'])
def add_comentario():
    data = request.get_json()
    texto = data.get('texto')
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentarios (texto, hora) VALUES (%s, %s)", (texto, hora))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Comentário adicionado com sucesso'}), 201

if __name__ == '__main__':
    app.run(debug=True)
