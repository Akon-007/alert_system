# Tactical Alert System

A Flask-based alert management system that generates and distributes security alerts in CAP (Common Alerting Protocol) XML format. The system includes a web interface for creating alerts and a simulator for monitoring alert delivery.

## Features

- **CAP XML Alert Generation**: Automatically generates alerts in Common Alerting Protocol format
- **Real-time Alert Monitoring**: Simulator interface polls for new alerts every second
- **Flexible Alert Types**: Support for circular and polygon area definitions
- **Multi-language Support**: Configurable language settings in alerts
- **Security-focused**: Designed for military/tactical security operations
- **Simple Web Interface**: Easy-to-use dashboard for alert creation and monitoring

## Project Structure

```
alert_system/
├── app.py                 # Flask application and alert logic
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Main alert creation interface
│   └── simulator.html    # Alert monitoring simulator
└── README.md             # This file
```

## Installation

1. **Clone or download the repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   - Main interface: `http://localhost:5000/`
   - Simulator: `http://localhost:5000/simulator`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main alert creation interface |
| `/simulator` | GET | Alert monitoring simulator |
| `/send_alert` | POST | Generate and send a new alert |
| `/check_alert` | GET | Check for latest alert (used by simulator) |
| `/reset` | POST | Reset alert state |

## Alert Format

Alerts are generated in CAP 1.2 (Common Alerting Protocol) XML format with the following structure:

- **Identifier**: Unique ID in format `MIL-NIG-{UUID}`
- **Sender**: Military operations email
- **Category**: Security threat classification
- **Urgency**: Immediate
- **Severity**: Extreme
- **Certainty**: Observed
- **Area**: Geographic area (circle or polygon coordinates)

## Configuration

The system can be customized by modifying:
- Alert category and message content
- Geographic area (circle or polygon coordinates)
- Language settings (default: en-US)
- Server host and port (currently `0.0.0.0:5000`)

## Requirements

- Python 3.7+
- Flask 3.0.0

## License

[Specify your license here]

## Support

For issues or questions, please contact the development team.
