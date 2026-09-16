from flask import Flask, request, jsonify, send_file, send_from_directory
import json
import os
import webbrowser
from threading import Timer

app = Flask(__name__)
STATE_FILE = 'windows_state.json'

@app.route('/')
def index():
    return send_file('windows.html')

@app.route('/files/<path:filename>')
def serve_files(filename):
    # Абсолютный путь к вашей рабочей директории
    base_dir = '/home/foxygamer/Документы/VSCode/'
    return send_from_directory(base_dir, filename)

@app.route('/api/state', methods=['GET', 'POST'])
def handle_state():
    if request.method == 'POST':
        state_data = request.json
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state_data, f, ensure_ascii=False, indent=4)
        return jsonify({"status": "success"})
    
    elif request.method == 'GET':
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                return jsonify(json.load(f))
        else:
            return jsonify({"error": "No state saved yet"}), 404

def open_browser():
    # Используем open_new_tab вместо open_new
    webbrowser.open_new_tab("http://127.0.0.1:5000/")

if __name__ == '__main__':
    # Запускаем таймер, который вызовет open_browser через 1 секунду
    Timer(1.0, open_browser).start()
    
    app.run(debug=True, port=5000, use_reloader=False)