# Single-Board IoT Project

This is an open-source IoT project designed for a single-board system like ESP32. The project manages Wi-Fi connectivity, sensors, relays, and user interaction via an LCD and keypad. It demonstrates a clean architecture suitable for small-scale IoT applications, with potential scalability for larger systems.

## Features

- **Wi-Fi Connectivity**: Connects to a network using user-provided credentials.
- **Sensor Management**: Reads and processes data from various sensors (e.g., temperature, humidity, light).
- **Relay Control**: Manages relays to control external devices.
- **Extensibility**: Modular design for adding new hardware or features.

## Requirements

- **Hardware**: NodeMCU-ESP32 or similar microcontroller.
- **Software**:
- - [MicroPython - Python 3.8+](https://micropython.org/)
  - [Thonny IDE](https://thonny.org/) or any MicroPython-compatible IDE.
- Libraries: `micropython-paho-mqtt`, `micropython-urequests`

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TechOnIt/single-board.git
   cd single-board
   ```
2. **Install required Python packages**
```
pip install paho-mqtt
```

3. **Flash MicroPython firmware to your board (if not already done):**
```
esptool.py --chip esp32 erase_flash
esptool.py --chip esp32 write_flash -z 0x1000 esp32-20220117-v1.18.bin
```
4. **Upload the project files to the board using Thonny or another supported method.**

## Usage

1. Power up the board and connect it to a computer or power source.
2. Configure the Wi-Fi credentials through the menu system displayed on the LCD.
3. The device will connect to the MQTT server and begin publishing sensor data.
4. Monitor sensor readings and control relays remotely through MQTT.

## Contributing

Contributions are welcome! If you'd like to report bugs, suggest features, or submit code, please open an issue or create a pull request.

## License

- [MicroPython](https://micropython.org/) for providing a lightweight and versatile Python implementation.
- The open-source community for their invaluable contributions.

### Notes:
- This README includes project highlights, setup instructions, and collaboration guidelines.
- The **Project Structure** section was excluded as requested.
- Customize the links (e.g., firmware or license) as necessary.
