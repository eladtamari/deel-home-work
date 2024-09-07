from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# External IP lookup service
IP_LOOKUP_SERVICE_URL = "https://ipinfo.io"

@app.route('/public-ip', methods=['POST'])
def get_public_ip():
    """_summary_
        The func recives requests in the format:
        curl -X POST http://<ip>:5000/reverse-ip \
        -H "Content-Type: application/json" \
        -d '{"ip": "1.3.4.5"}'
        
        1. Verfies that the requests contins an ip address
        2. Verfiy that the format of the IP correct

    Returns:
        Revered IP
    """
    data = request.get_json()
    ip_address = data.get('ip')

    if not ip_address:
        return jsonify({'error': 'IP address not provided'}), 400

    # Use external service to get public IP information
    try:
        response = requests.get(f"{IP_LOOKUP_SERVICE_URL}/{ip_address}/json")
        response.raise_for_status()
        ip_info = response.json()
        return jsonify(ip_info)
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0")

