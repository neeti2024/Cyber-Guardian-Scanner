from flask import Flask, jsonify, request
from flask_cors import CORS
from urllib.parse import urlparse
import time

app = Flask(__name__)
CORS(app)

@app.after_request
def add_headers(response):
    response.headers['Security-Headers'] = 'max-age=3600; includeSubDomains'
    return response

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

@app.route('/scan', methods=['POST'])
def scan_website():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL required"}), 400

    target_url = data['url'].strip()
    
    if not validate_url(target_url):
        return jsonify({"error": "Invalid URL"}), 400

    time.sleep(2)  # Simulate scan
    
    results = [
        {
            "name": "SQL Injection",
            "severity": "critical",
            "description": "Unsanitized user input detected",
            "solution": "Use parameterized queries"
        },
        {
            "name": "XSS Vulnerability",
            "severity": "high",
            "description": "Missing input sanitization",
            "solution": "Implement Content Security Policy"
        }
    ]

    return jsonify({
        "status": "completed",
        "vulnerabilities": results
    })

if __name__ == '__main__':
    app.run(port=5000)