from flask import Flask, render_template, request, jsonify
import xml.etree.ElementTree as ET
from datetime import datetime
import uuid

app = Flask(__name__)

# This stores the latest alert so the simulator can check for it
latest_alert = {
    "active": False,
    "message": "",
    "category": "",
    "xml": ""
}

def generate_cap_xml(data):
    alert_id = str(uuid.uuid4())
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S-01:00")
    
    alert = ET.Element("alert", xmlns="urn:oasis:names:tc:emergency:cap:1.2")
    ET.SubElement(alert, "identifier").text = f"MIL-NIG-{alert_id}"
    ET.SubElement(alert, "sender").text = "military.ops@nigeria.gov.ng"
    ET.SubElement(alert, "sent").text = now
    ET.SubElement(alert, "status").text = "Actual"
    ET.SubElement(alert, "msgType").text = "Alert"
    ET.SubElement(alert, "scope").text = "Public"
    
    info = ET.SubElement(alert, "info")
    ET.SubElement(info, "language").text = data.get('language', 'en-US')
    ET.SubElement(info, "category").text = "Security"
    ET.SubElement(info, "event").text = data.get('category', 'Security Threat')
    ET.SubElement(info, "urgency").text = "Immediate"
    ET.SubElement(info, "severity").text = "Extreme"
    ET.SubElement(info, "certainty").text = "Observed"
    ET.SubElement(info, "headline").text = f"IMMINENT {data.get('category').upper()} THREAT"
    ET.SubElement(info, "description").text = data.get('message')
    
    area = ET.SubElement(info, "area")
    ET.SubElement(area, "areaDesc").text = data.get('areaDesc', 'Target Zone')
    
    if data.get('type') == 'circle':
        ET.SubElement(area, "circle").text = data.get('coords')
    elif data.get('type') == 'polygon':
        ET.SubElement(area, "polygon").text = data.get('coords')

    return ET.tostring(alert, encoding='utf-8', method='xml').decode('utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulator')
def simulator():
    return render_template('simulator.html')

@app.route('/send_alert', methods=['POST'])
def send_alert():
    global latest_alert
    data = request.json
    cap_xml = generate_cap_xml(data)
    
    # Update the global variable
    latest_alert = {
        "active": True,
        "message": data.get('message'),
        "category": data.get('category'),
        "xml": cap_xml
    }
    return jsonify({"status": "success", "xml": cap_xml})

@app.route('/check_alert', methods=['GET'])
def check_alert():
    # The simulator calls this every second to see if there's a new alert
    return jsonify(latest_alert)

@app.route('/reset', methods=['POST'])
def reset():
    global latest_alert
    latest_alert = {"active": False, "message": "", "category": "", "xml": ""}
    return jsonify({"status": "reset"})

if __name__ == '__main__':
    print("\n" + "="*50)
    print("TACTICAL ALERT SYSTEM ONLINE")
    print("Open http://localhost:5000 in your browser")
    print("="*50 + "\n")
    app.run(debug=False, port=5000, host='0.0.0.0')