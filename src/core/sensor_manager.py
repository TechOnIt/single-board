import threading
import time
from hardware.sensor_reader import SensorReader  # Import sensor_reader from hardware

class SensorManager:
    def __init__(self):
        """
        Initialize the sensor manager.
        """
        self.sensor_reader = SensorReader()
        self.running = False
        self.sensors_data = {}
        self.update_interval = 5  # Update interval in seconds
        self.thread = None

    def configure_sensors(self, sensor_configs):
        """
        Configure sensors with provided settings.

        :param sensor_configs: List of sensor configurations (type, pin, etc.)
        """
        self.sensor_reader.configure_sensors(sensor_configs)

    def start(self):
        """
        Start the sensor manager to periodically read sensor data.
        """
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._read_sensors_loop, daemon=True)
            self.thread.start()

    def stop(self):
        """
        Stop the sensor manager.
        """
        self.running = False
        if self.thread:
            self.thread.join()

    def _read_sensors_loop(self):
        """
        Periodically read sensor data in a loop.
        """
        while self.running:
            self.read_all_sensors()
            time.sleep(self.update_interval)

    def read_all_sensors(self):
        """
        Read all configured sensors and update their values.
        """
        self.sensors_data = self.sensor_reader.read_all()
        print("Updated sensor data:", self.sensors_data)

    def get_sensor_data(self, sensor_name):
        """
        Retrieve data for a specific sensor.

        :param sensor_name: Name of the sensor
        :return: Sensor data if available, otherwise None
        """
        return self.sensors_data.get(sensor_name, None)
