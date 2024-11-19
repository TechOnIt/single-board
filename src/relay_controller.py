from machine import Pin
import time

class RelayController:
    def __init__(self, pin_numbers):
        """
        Initialize relay pins.
        :param pin_numbers: List of pin numbers to manage relays.
        """
        self.relay_pins = {}
        for pin_number in pin_numbers:
            self.relay_pins[pin_number] = Pin(pin_number, Pin.OUT)
            self.relay_pins[pin_number].value(0)  # Ensure all relays are off initially

    def turn_on(self, pin_number):
        """
        Turn on a specific relay.
        :param pin_number: Pin number to turn on.
        """
        if pin_number in self.relay_pins:
            self.relay_pins[pin_number].value(1)
            print(f"Relay on pin {pin_number} is now ON.")
        else:
            print(f"Pin {pin_number} is not configured.")

    def turn_off(self, pin_number):
        """
        Turn off a specific relay.
        :param pin_number: Pin number to turn off.
        """
        if pin_number in self.relay_pins:
            self.relay_pins[pin_number].value(0)
            print(f"Relay on pin {pin_number} is now OFF.")
        else:
            print(f"Pin {pin_number} is not configured.")

    def turn_on_range(self, pin_range):
        """
        Turn on a range of relays.
        :param pin_range: List or range of pin numbers to turn on.
        """
        for pin_number in pin_range:
            self.turn_on(pin_number)

    def turn_off_range(self, pin_range):
        """
        Turn off a range of relays.
        :param pin_range: List or range of pin numbers to turn off.
        """
        for pin_number in pin_range:
            self.turn_off(pin_number)

# Example usage
if __name__ == "__main__":
    # Initialize the relay controller with pin numbers
    relay_controller = RelayController([2, 4, 5, 12, 14])

    # Turn on a single relay
    relay_controller.turn_on(4)

    # Turn off a single relay
    relay_controller.turn_off(4)

    # Turn on a range of relays
    relay_controller.turn_on_range([2, 5, 12])

    # Turn off a range of relays
    relay_controller.turn_off_range([2, 5, 12])

    # Delay to observe relay changes
    time.sleep(5)
