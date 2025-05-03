import time

try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    from gpio_mock import GPIO

# Setup
print("[INFO] Setting GPIO mode to BCM")
GPIO.setmode(GPIO.BCM)

print("[INFO] Setting up pin 18 as OUTPUT")
GPIO.setup(18, GPIO.OUT)

print("[INFO] Turning pin 18 ON (HIGH)")
GPIO.output(18, GPIO.HIGH)

# Optional: blink it for verification
for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    print(f"[DEBUG] Pin 18 HIGH ({i+1}/5)")
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    print(f"[DEBUG] Pin 18 LOW ({i+1}/5)")
    time.sleep(1)

GPIO.cleanup()
print("[INFO] GPIO cleanup done.")
