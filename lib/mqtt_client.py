# mqtt_client.py
import paho.mqtt.client as mqtt
import json

# Hardcoded API and Secret Keys
API_KEY = "your_api_key_here"
SECRET_KEY = "your_secret_key_here"

# MQTT Server Address
MQTT_SERVER = "board.techonit.org"
MQTT_PORT = 1883  # Default port for MQTT (non-secure). Use 8883 for secure connections.
MQTT_TOPIC_SENSOR = "home/sensors"
MQTT_TOPIC_RELAY = "home/relays"

# Callback function when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to relay topic when connected
    client.subscribe(MQTT_TOPIC_RELAY)

# Callback function when a message is received from the server
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")
    # Process the relay commands from the server
    process_relay_command(msg.payload.decode())

# Function to process relay commands
def process_relay_command(command):
    print(f"Processing command: {command}")
    # Here, you would interact with the relays (e.g., turn on/off)
    # Example: if command == "turn_on":
    #            relay_on_function()

# Function to send sensor data to the server
def send_sensor_data(client, sensor_type, sensor_value):
    payload = {
        "sensor_type": sensor_type,
        "sensor_value": sensor_value
    }
    client.publish(MQTT_TOPIC_SENSOR, json.dumps(payload))
    print(f"Sent sensor data: {payload}")

# Function to send relay command to the server
def send_relay_command(client, relay_id, action):
    payload = {
        "relay_id": relay_id,
        "action": action  # Example: "on", "off"
    }
    client.publish(MQTT_TOPIC_RELAY, json.dumps(payload))
    print(f"Sent relay command: {payload}")

# Create the MQTT client instance
client = mqtt.Client()

# Set the username and password for MQTT authentication (API key and secret)
client.username_pw_set(API_KEY, SECRET_KEY)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop to handle incoming messages
client.loop_start()

# Example usage: Send some sensor data
send_sensor_data(client, "temperature", 23.5)
send_sensor_data(client, "humidity", 60)

# Example usage: Send a relay command
send_relay_command(client, 1, "on")

# To keep the script running, you can use:
# client.loop_forever() to continuously check for incoming messages (if you prefer not to use loop_start())
