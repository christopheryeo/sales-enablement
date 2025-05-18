from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__, static_folder='../', static_url_path='')

# Serve the main training page
@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'sales-enablement/templates/index.html')

# Serve any static file (html, js, css, etc.)
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

# Example POST endpoint for progress or quiz submissions
@app.route('/training', methods=['POST'])
def training_post():
    data = request.get_json() or request.form
    # You can process/store data here
    return jsonify({'status': 'success', 'received': data})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
