from flask import Flask, request, jsonify, render_template_string
import os
import signal
import sys

# Inițializează aplicația Flask
app = Flask(__name__)

# HTML-ul trimis la accesarea rădăcinii (/) pentru testare interactivă
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator API</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
        .result { margin: 20px 0; padding: 10px; background: #f0f0f0; }
        button { padding: 5px 10px; }
        input { margin: 5px; padding: 5px; }
    </style>
</head>
<body>
    <h1>Calculator API</h1>
    <div>
        <h3>Add or Multiply Numbers</h3>
        <input type="text" id="numbers" placeholder="Enter numbers (comma-separated)">
        <select id="operation">
            <option value="add">Add</option>
            <option value="multiply">Multiply</option>
        </select>
        <button onclick="calculate()">Calculate</button>
    </div>
    <div class="result" id="result"></div>

    <script>
        async function calculate() {
            const numbers = document.getElementById('numbers').value.split(',').map(Number);
            const operation = document.getElementById('operation').value;

            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({operation, numbers})
            });

            const data = await response.json();
            document.getElementById('result').innerText =
                data.result !== undefined ? `Result: ${data.result}` : `Error: ${data.error}`;
        }
    </script>
</body>
</html>
"""

# Ruta principală care returnează interfața HTML
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Ruta POST pentru calcul
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Validare input
    if not data or 'operation' not in data or 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    operation = data['operation']
    numbers = data['numbers']

    # Aplica operația cerută
    if operation == 'add':
        result = sum(numbers)
    elif operation == 'multiply':
        result = 1
        for num in numbers:
            result *= num
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

# Funcție apelată la oprirea containerului pentru shutdown curat
def handle_shutdown(signum, frame):
    print("Shutting down the Flask app cleanly...")
    sys.exit(0)

# Legare semnale SIGTERM și SIGINT la funcția de shutdown
signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)

# Pornirea aplicației Flask pe portul definit (default 8080)
if __name__ == '__main__':
    port = int(os.environ.get("APP_PORT", 8080))  # Preia portul din variabilă de mediu dacă există
    app.run(host='0.0.0.0', port=port)
