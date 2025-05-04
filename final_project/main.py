import os
import time
import logging

# Read environment variables
use_mock = os.getenv("USE_GPIO_MOCK", "false").lower() == "true"
pin_definitions = os.getenv("PINS", "")
log_level = os.getenv("LOG_LEVEL", "INFO").upper()

# Set up logging
logging.basicConfig(level=getattr(logging, log_level), format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("gpio-app")

# Import GPIO module
if use_mock:
    from gpio_mock import GPIO
    logger.info("Using MOCK GPIO")
else:
    import RPi.GPIO as GPIO
    logger.info("Using REAL GPIO")

# Parse pins and their modes
pin_map = {}
for item in pin_definitions.split(","):
    try:
        pin_str, mode_str = item.strip().split(":")
        pin = int(pin_str)
        mode = GPIO.OUT if mode_str.upper() == "OUT" else GPIO.IN
        pin_map[pin] = mode
    except ValueError:
        logger.warning(f"Invalid pin definition: '{item}' (expected format pin:MODE)")

# GPIO setup
GPIO.setmode(GPIO.BCM)
for pin, mode in pin_map.items():
    GPIO.setup(pin, mode)
    mode_name = "OUTPUT" if mode == GPIO.OUT else "INPUT"
    logger.info(f"Configured pin {pin} as {mode_name}")

# Example: Toggle output pins, read input pins
for i in range(2):
    for pin, mode in pin_map.items():
        if mode == GPIO.OUT:
            GPIO.output(pin, GPIO.HIGH)
            logger.info(f"Pin {pin} set HIGH")
    time.sleep(1)
    for pin, mode in pin_map.items():
        if mode == GPIO.OUT:
            GPIO.output(pin, GPIO.LOW)
            logger.info(f"Pin {pin} set LOW")
        elif mode == GPIO.IN:
            value = GPIO.input(pin)
            logger.info(f"Pin {pin} READ value = {value}")
    time.sleep(1)

GPIO.cleanup()
logger.info("GPIO cleanup done.")

