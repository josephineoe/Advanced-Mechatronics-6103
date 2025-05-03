try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    # Fallback to mock when not on Raspberry Pi
    from gpio_mock import GPIO

# Example usage
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
