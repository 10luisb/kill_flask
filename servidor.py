from flask import Flask, request, jsonify
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/kill_process', methods=['POST'])
def kill_process():
    data = request.get_json()
    
    if 'pid' in data:
        try:
            pid = int(data['pid'])
            os.kill(pid, 9)
            return jsonify({'message': f"Proceso con PID {pid} terminado."})
        except OSError as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'No se proporcionó un PID válido.'})

if __name__ == '__main__':
    app.run()