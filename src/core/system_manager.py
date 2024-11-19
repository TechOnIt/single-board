import asyncio
import threading
from wifi_manager import WiFiManager
from mqtt_client import MQTTClient
from sensor_manager import SensorManager
from relay_manager import RelayManager

class SystemManager:
    def __init__(self):
        self.wifi_manager = WiFiManager()
        self.mqtt_client = MQTTClient()
        self.sensor_manager = SensorManager()
        self.relay_manager = RelayManager()

    def start(self):
        # Connect to Wi-Fi
        if not self.wifi_manager.connect():
            print("Failed to connect to Wi-Fi!")
            return

        # Connect to MQTT
        if not self.mqtt_client.connect():
            print("Failed to connect to MQTT!")
            return

        # Start sensor and relay management in separate threads
        threading.Thread(target=self.sensor_manager.read_sensors, daemon=True).start()
        threading.Thread(target=self.relay_manager.manage_relays, daemon=True).start()

        # Fetch configuration and listen for commands
        asyncio.run(self.fetch_configs())

    async def fetch_configs(self):
        # Fetch sensor and relay configurations from MQTT server
        await self.mqtt_client.subscribe("sensor/config")
        await self.mqtt_client.subscribe("relay/config")
        
        # Process sensor data and relay commands asynchronously
        while True:
            sensor_data = await self.mqtt_client.receive("sensor/data")
            relay_data = await self.mqtt_client.receive("relay/data")
            
            # Process and update sensor data
            self.sensor_manager.process_sensor_data(sensor_data)
            
            # Apply relay commands
            self.relay_manager.apply_relay_commands(relay_data)

if __name__ == "__main__":
    system_manager = SystemManager()
    system_manager.start()
