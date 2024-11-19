# sensor_value_calculator.py
"""
Module for calculating and converting raw sensor data to human-readable units.
This module supports multiple types of sensors like temperature, humidity, and soil moisture.
"""

# Example function to calculate temperature in Celsius from a raw value
def calculate_temperature(raw_value, sensor_type="DHT11"):
    """
    Convert raw temperature sensor data to Celsius.
    Args:
        raw_value (int/float): Raw sensor value (e.g., raw ADC or digital output)
        sensor_type (str): Type of sensor (e.g., "DHT11", "DHT22")
    
    Returns:
        float: Temperature in Celsius
    """
    if sensor_type == "DHT11":
        # Example conversion for DHT11, where raw_value is typically in 0.1C (e.g., raw_value * 0.1)
        return raw_value / 10.0
    elif sensor_type == "DHT22":
        # Example for DHT22 sensor, assuming a different scaling factor
        return raw_value * 0.1
    else:
        raise ValueError(f"Unsupported sensor type: {sensor_type}")

# Example function to calculate humidity as percentage from raw value
def calculate_humidity(raw_value, sensor_type="DHT11"):
    """
    Convert raw humidity sensor data to percentage.
    Args:
        raw_value (int/float): Raw sensor value (e.g., raw ADC or digital output)
        sensor_type (str): Type of sensor (e.g., "DHT11", "DHT22")
    
    Returns:
        float: Humidity in percentage
    """
    if sensor_type == "DHT11":
        # For DHT11 sensor, raw value is given directly as a percentage (0-100)
        return raw_value
    elif sensor_type == "DHT22":
        # Example for DHT22, where raw_value needs to be scaled
        return raw_value * 0.1
    else:
        raise ValueError(f"Unsupported sensor type: {sensor_type}")

# Example function to calculate soil moisture percentage from raw value
def calculate_soil_moisture(raw_value, max_value=1024):
    """
    Convert raw soil moisture sensor data to percentage.
    Args:
        raw_value (int): Raw sensor value (e.g., from an analog pin)
        max_value (int): Maximum possible value from the sensor (default 1024 for 10-bit ADC)
    
    Returns:
        float: Soil moisture percentage (0% = dry, 100% = fully wet)
    """
    return (raw_value / max_value) * 100

# Example function to convert light intensity (e.g., from a photoresistor) to percentage
def calculate_light_intensity(raw_value, max_value=1024):
    """
    Convert raw light sensor data to percentage of light intensity.
    Args:
        raw_value (int): Raw sensor value (e.g., from an analog pin)
        max_value (int): Maximum possible value from the sensor (default 1024 for 10-bit ADC)
    
    Returns:
        float: Light intensity percentage
    """
    return (raw_value / max_value) * 100

# Example function to calculate air quality index (AQI) from raw gas sensor value
def calculate_air_quality(raw_value, max_value=500):
    """
    Convert raw gas sensor data to air quality index.
    Args:
        raw_value (int): Raw gas sensor value (e.g., from MQ series sensor)
        max_value (int): Maximum value the sensor can output (default 500)
    
    Returns:
        float: Air quality index (lower is better)
    """
    return (raw_value / max_value) * 100
