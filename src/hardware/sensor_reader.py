from machine import Pin, ADC
import time

class SensorReader:
    def __init__(self, analog_pins=None, digital_pins=None):
        """
        Initialize the sensor reader.
        :param analog_pins: List of analog pin numbers (for ADC sensors).
        :param digital_pins: List of digital pin numbers (for digital sensors).
        """
        self.analog_sensors = {}
        self.digital_sensors = {}

        # Initialize analog pins
        if analog_pins:
            for pin in analog_pins:
                self.analog_sensors[pin] = ADC(Pin(pin))
                self.analog_sensors[pin].atten(ADC.ATTN_11DB)  # Configure range for ADC (0-3.3V)

        # Initialize digital pins
        if digital_pins:
            for pin in digital_pins:
                self.digital_sensors[pin] = Pin(pin, Pin.IN)

    def read_analog(self, pin_number):
        """
        Read value from an analog sensor.
        :param pin_number: Pin number of the analog sensor.
        :return: Analog sensor value (0-4095).
        """
        if pin_number in self.analog_sensors:
            value = self.analog_sensors[pin_number].read()
            print(f"Analog sensor on pin {pin_number} reads: {value}")
            return value
        else:
            print(f"Analog pin {pin_number} is not configured.")
            return None

    def read_digital(self, pin_number):
        """
        Read value from a digital sensor.
        :param pin_number: Pin number of the digital sensor.
        :return: Digital sensor value (0 or 1).
        """
        if pin_number in self.digital_sensors:
            value = self.digital_sensors[pin_number].value()
            print(f"Digital sensor on pin {pin_number} reads: {value}")
            return value
        else:
            print(f"Digital pin {pin_number} is not configured.")
            return None

    def read_all_analog(self):
        """
        Read all configured analog sensors.
        :return: Dictionary with pin numbers and their values.
        """
        results = {}
        for pin in self.analog_sensors:
            results[pin] = self.read_analog(pin)
        return results

    def read_all_digital(self):
        """
        Read all configured digital sensors.
        :return: Dictionary with pin numbers and their values.
        """
        results = {}
        for pin in self.digital_sensors:
            results[pin] = self.read_digital(pin)
        return results

# Example usage
if __name__ == "__main__":
    # Initialize the sensor reader with example analog and digital pins
    sensor_reader = SensorReader(analog_pins=[34, 35], digital_pins=[14, 27])

    while True:
        # Read and print values from all sensors
        print("Analog Sensor Values:", sensor_reader.read_all_analog())
        print("Digital Sensor Values:", sensor_reader.read_all_digital())
        
        # Delay between readings
        time.sleep(2)
