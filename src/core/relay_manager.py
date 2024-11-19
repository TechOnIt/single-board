from relay_controller import RelayController

class RelayManager:
    def __init__(self):
        self.relays = {}

    def initialize_relays(self, relay_config):
        """
        Initializes relays based on the provided configuration.
        :param relay_config: Dictionary containing relay pin configurations.
        """
        for relay_name, pin in relay_config.items():
            self.relays[relay_name] = RelayController(pin)
        print("Relays initialized:", self.relays.keys())

    def apply_commands(self, commands):
        """
        Applies commands to relays (e.g., turn on/off).
        :param commands: List of dictionaries with 'relay_name' and 'state'.
        """
        for command in commands:
            relay_name = command.get("relay_name")
            state = command.get("state")
            if relay_name in self.relays:
                if state == "on":
                    self.relays[relay_name].turn_on()
                elif state == "off":
                    self.relays[relay_name].turn_off()
            else:
                print(f"Relay '{relay_name}' not found.")

    def turn_all_off(self):
        """Turns off all relays."""
        for relay in self.relays.values():
            relay.turn_off()

    def turn_all_on(self):
        """Turns on all relays."""
        for relay in self.relays.values():
            relay.turn_on()

# Example usage:
# relay_manager = RelayManager()
# relay_manager.initialize_relays({"relay1": 5, "relay2": 6})
# relay_manager.apply_commands([{"relay_name": "relay1", "state": "on"}])
