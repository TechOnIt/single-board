class SensorValueCalculator:
    def __init__(self):
        pass

    def calculate_temperature(self, raw_value, sensor_type="DHT11"):
        """
        Convert raw temperature value to degrees Celsius or Fahrenheit.
        Depends on sensor type, for example DHT11, DHT22, etc.
        :param raw_value: Raw sensor reading.
        :param sensor_type: The type of temperature sensor (e.g., DHT11, DHT22).
        :return: Calculated temperature in Celsius or Fahrenheit.
        """
        if sensor_type == "DHT11":
            # Example: DHT11 gives raw integer value directly as celsius
            temperature_celsius = raw_value
        elif sensor_type == "DHT22":
            # DHT22 may provide raw temperature that needs conversion
            temperature_celsius = raw_value / 10.0  # Convert raw to real temperature
        else:
            raise ValueError(f"Unsupported sensor type {sensor_type} for temperature.")
        return temperature_celsius

    def calculate_humidity(self, raw_value, sensor_type="DHT11"):
        """
        Convert raw humidity value to percentage.
        :param raw_value: Raw sensor reading.
        :param sensor_type: The type of humidity sensor (e.g., DHT11, DHT22).
        :return: Calculated humidity in percentage.
        """
        if sensor_type == "DHT11" or sensor_type == "DHT22":
            humidity = raw_value  # DHT11/DHT22 give raw values in percentage
        else:
            raise ValueError(f"Unsupported sensor type {sensor_type} for humidity.")
        return humidity

    def calculate_soil_moisture(self, raw_value, min_value=0, max_value=1023):
        """
        Calculate soil moisture percentage from the raw analog sensor value.
        :param raw_value: Raw sensor reading.
        :param min_value: The minimum analog reading for dry soil.
        :param max_value: The maximum analog reading for wet soil.
        :return: Calculated soil moisture percentage.
        """
        moisture = (raw_value - min_value) / (max_value - min_value) * 100
        return moisture

    def calculate_light_intensity(self, raw_value, sensor_type="LDR"):
        """
        Calculate light intensity from raw sensor values (like LDR).
        :param raw_value: Raw sensor reading.
        :param sensor_type: The type of light sensor (e.g., LDR).
        :return: Calculated light intensity (lux).
        """
        if sensor_type == "LDR":
            # Raw LDR value can be translated to light intensity (lux) using a formula or lookup
            light_intensity = raw_value  # This could be scaled or mapped if necessary
        else:
            raise ValueError(f"Unsupported sensor type {sensor_type} for light intensity.")
        return light_intensity

    def calculate_air_quality(self, raw_value, sensor_type="MQ7"):
        """
        Calculate air quality index based on raw sensor value.
        :param raw_value: Raw air quality sensor value.
        :param sensor_type: The air quality sensor (e.g., MQ7).
        :return: Calculated air quality (AQI).
        """
        if sensor_type == "MQ7":
            # Example: MQ7 sensor needs a formula to calculate CO levels
            air_quality = raw_value * 0.1  # Placeholder scaling factor
        else:
            raise ValueError(f"Unsupported sensor type {sensor_type} for air quality.")
        return air_quality

    def calculate_vibration(self, raw_value, threshold=100):
        """
        Detect if there is significant vibration or earthquake.
        :param raw_value: Raw vibration data.
        :param threshold: Threshold to determine if the vibration is significant.
        :return: Boolean indicating if a vibration was detected.
        """
        vibration_detected = raw_value > threshold
        return vibration_detected

    def calculate_smell(self, raw_value, sensor_type="MQ3"):
        """
        Calculate smell detection (e.g., alcohol, gas) based on sensor readings.
        :param raw_value: Raw sensor value.
        :param sensor_type: The smell sensor (e.g., MQ3).
        :return: Calculated concentration of the smell.
        """
        if sensor_type == "MQ3":
            smell_concentration = raw_value * 0.5  # Placeholder scaling factor for alcohol detection
        else:
            raise ValueError(f"Unsupported sensor type {sensor_type} for smell detection.")
        return smell_concentration

    def calculate_distance(self, raw_value, unit="cm"):
        """
        Convert raw distance sensor value to actual distance.
        :param raw_value: Raw sensor value from distance sensor.
        :param unit: Distance unit (mm, cm, m).
        :return: Calculated distance in specified units.
        """
        distance = raw_value / 10.0  # Example scaling (raw_value is in mm by default)
        if unit == "mm":
            distance = raw_value  # Raw value is already in mm
        elif unit == "cm":
            distance = raw_value / 10.0  # Convert mm to cm
        elif unit == "m":
            distance = raw_value / 1000.0  # Convert mm to meters
        else:
            raise ValueError(f"Unsupported unit {unit} for distance.")
        return distance
