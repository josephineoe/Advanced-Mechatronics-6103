from machine import Pin, I2C, Timer
import time
import math

# Constants
RAD_TO_DEG = 57.295779513
DEG_TO_RAD = 0.0174533
FILTER_ALPHA = 0.05  # Complementary filter coefficient

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
print("Detected I2C devices:", [hex(addr) for addr in i2c.scan()])

# IMU Initialization
def init_sensors():
    # Accelerometer (0x19) - LSM303DLHC
    i2c.writeto_mem(0x19, 0x20, bytes([0x57]))  # 100Hz, XYZ enabled
    i2c.writeto_mem(0x19, 0x23, bytes([0x00]))  # ±2g range
    
    # Magnetometer (0x1e) - LSM303DLHC
    i2c.writeto_mem(0x1e, 0x00, bytes([0x10]))  # 15Hz output rate
    i2c.writeto_mem(0x1e, 0x01, bytes([0x20]))  # ±1.3 Gauss
    i2c.writeto_mem(0x1e, 0x02, bytes([0x00]))  # Continuous mode
    
    # Gyroscope (try both addresses)
    try:
        i2c.writeto_mem(0x6b, 0x20, bytes([0x0F]))  # 95Hz, XYZ enabled
        gyro_addr = 0x6b
    except OSError:
        i2c.writeto_mem(0x69, 0x20, bytes([0x0F]))
        gyro_addr = 0x69
    return gyro_addr

gyro_addr = init_sensors()

# Sensor Reading Functions
def read_accel():
    data = i2c.readfrom_mem(0x19, 0x28 | 0x80, 6)
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]
    return (x/16384.0, y/16384.0, z/16384.0)  # ±2g range

def read_gyro():
    data = i2c.readfrom_mem(gyro_addr, 0x28 | 0x80, 6)
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]
    return (x*0.00875, y*0.00875, z*0.00875)  # ±245dps range

# Orientation Tracking
f_phi = 0.0  # Roll (X)
f_theta = 0.0  # Pitch (Y)

def update_orientation():
    global f_phi, f_theta
    
    # Read sensor data
    ax, ay, az = read_accel()
    gx, gy, gz = read_gyro()
    
    # Calculate angles from accelerometer
    a_phi = math.atan2(ay, az)  # Roll
    a_theta = math.atan2(-ax, math.sqrt(ay**2 + az**2))  # Pitch
    
    # Integrate gyroscope data (convert to radians)
    gy_phi = f_phi + (gx * DEG_TO_RAD * 0.001)  # dt ≈ 1ms
    gy_theta = f_theta + (gy * DEG_TO_RAD * 0.001)
    
    # Complementary filter
    f_phi = FILTER_ALPHA * gy_phi + (1.0 - FILTER_ALPHA) * a_phi
    f_theta = FILTER_ALPHA * gy_theta + (1.0 - FILTER_ALPHA) * a_theta
    
    # Convert to degrees
    roll = f_phi * RAD_TO_DEG
    pitch = f_theta * RAD_TO_DEG
    
    # Print results
    print(f"Roll: {roll:.2f}°, Pitch: {pitch:.2f}°")
    print(f"Accel: {ax:.2f}, {ay:.2f}, {az:.2f} g")
    print(f"Gyro: {gx:.2f}, {gy:.2f}, {gz:.2f} °/s")
    print("------------------")

# Main loop
last_time = time.ticks_ms()
while True:
    current_time = time.ticks_ms()
    dt = (current_time - last_time) / 1000.0  # Convert to seconds
    last_time = current_time
    
    update_orientation()
    time.sleep(1)  