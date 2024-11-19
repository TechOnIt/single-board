import threading
import time
from wifi_manager import WiFiManager
from mqtt_client import MQTTClient
from sensor_manager import SensorManager
from relay_manager import RelayManager

class SystemManager:
    def __init__(self):
        # Initialize components
        self.wifi_manager = WiFiManager()
        self.mqtt_client = MQTTClient()
        self.sensor_manager = SensorManager()
        self.relay_manager = RelayManager()

        # Threading or loop control variables
        self.running = True

    def connect_to_wifi(self):
        print("Connecting to Wi-Fi...")
        if not self.wifi_manager.connect():
            raise Exception("Failed to connect to Wi-Fi.")
        print("Connected to Wi-Fi.")

    def setup_mqtt(self):
        print("Setting up MQTT client...")
        self.mqtt_client.connect()
        self.mqtt_client.subscribe("config/sensors")
        self.mqtt_client.subscribe("config/relays")
        self.mqtt_client.subscribe("commands/relays")
        print("MQTT client setup complete.")

    def fetch_configurations(self):
        print("Fetching sensor and relay configurations...")
        sensor_config = self.mqtt_client.get_config("config/sensors")
        relay_config = self.mqtt_client.get_config("config/relays")
        self.sensor_manager.initialize_sensors(sensor_config)
        self.relay_manager.initialize_relays(relay_config)

    def process_sensor_data(self):
        while self.running:
            sensor_data = self.sensor_manager.read_all_sensors()
            print("Sensor Data:", sensor_data)
            self.mqtt_client.publish("data/sensors", sensor_data)
            time.sleep(2)  # Adjust frequency as needed

    def process_relay_commands(self):
        while self.running:
            commands = self.mqtt_client.get_commands("commands/relays")
            if commands:
                self.relay_manager.apply_commands(commands)
            time.sleep(1)  # Adjust frequency as needed

    def start(self):
        try:
            # Step 1: Connect to Wi-Fi
            self.connect_to_wifi()

            # Step 2: Set up MQTT client
            self.setup_mqtt()

            # Step 3: Fetch configurations
            self.fetch_configurations()

            # Step 4: Start sensor and relay processing in parallel
            sensor_thread = threading.Thread(target=self.process_sensor_data)
            relay_thread = threading.Thread(target=self.process_relay_commands)
            sensor_thread.start()
            relay_thread.start()

            # Step 5: Lifecycle loop
            while self.running:
                time.sleep(1)  # Keep the main thread alive

            # Wait for threads to finish
            sensor_thread.join()
            relay_thread.join()

        except KeyboardInterrupt:
            print("Shutting down system...")
            self.running = False
        except Exception as e:
            print(f"Error occurred: {e}")
            self.running = False

if __name__ == "__main__":
    manager = SystemManager()
    manager.start()
